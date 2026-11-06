#!/usr/bin/env python3
"""Run all local checks and write auditable reports without remote access."""
from __future__ import annotations
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import check_cofactor
import check_full_channel
import check_repository

def main() -> None:
    root=Path(__file__).resolve().parents[1]
    output=root/'verification/output'
    output.mkdir(exist_ok=True)
    results={'cofactor':check_cofactor.run(),'full_channel':check_full_channel.run(),
             'repository':check_repository.run()}
    hashes={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest()
            for p in root.rglob('*') if p.is_file() and '.git' not in p.parts
            and '__pycache__' not in p.parts and output not in p.parents}
    summary={'status':'pass','observed_at':datetime.now(timezone.utc).isoformat(),
             'python':platform.python_version(),'numpy':np.__version__,'source_sha256':hashes,
             'checks':results,'hosted_rendering':'not tested by this command'}
    (output/'local-checks.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    for name,r in results.items():
        print(f"PASS: {name}")
        if name=='full_channel': print(f"  {r['case_count']} physical-channel cases")
    print('PASS: all local checks')

if __name__=='__main__': main()
