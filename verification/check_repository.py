#!/usr/bin/env python3
"""Source, navigation and common-learning checks; not a hosted render test."""
from __future__ import annotations
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def anchors(text: str) -> set[str]:
    result = set(re.findall(r'<a\s+id="([^"]+)"', text))
    used: dict[str,int] = {}
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*$', text, re.M):
        title = re.sub(r'[`*_]', '', title).lower()
        slug = re.sub(r'[^\w\- ]', '', title).replace(' ', '-')
        count = used.get(slug, 0)
        used[slug] = count + 1
        result.add(slug if not count else f'{slug}-{count}')
    return result

def run() -> dict:
    errors=[]
    required=['README.md','science/README.md','science/model.md','science/construction.md',
              'science/converse.md','science/boundaries.md','learning/README.md',
              'learning/WATROUS_BRIDGE.md','learning/WORKED_EXAMPLE.md','learning/MILESTONES.md',
              'references/RELATED_WORK.md','references/references.bib','verification/README.md',
              'verification/requirements.txt','verification/run_all.py','llms.txt']
    for name in required:
        if not (ROOT/name).is_file(): errors.append(f'Missing {name}')
    md=list(ROOT.rglob('*.md'))
    link_count=0
    formula_count=0
    for path in md:
        source=path.read_text(encoding='utf-8')
        # The source inventory is intentionally simple and is not GitHub's parser.
        formula_count += len(re.findall(r'^```math\s*\n',source,re.M))
        if r'\(' in source or r'\[' in source: errors.append(f'Non-GitHub math delimiter: {path.relative_to(ROOT)}')
        if len(re.findall(r'^```',source,re.M))%2: errors.append(f'Unbalanced fence: {path.name}')
        stripped=re.sub(r'```.*?```','',source,flags=re.S)
        if stripped.count('$')%2: errors.append(f'Odd dollar count: {path.name}')
        formula_count += stripped.count('$')//2
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', stripped):
            parsed=urlsplit(target)
            if parsed.scheme or parsed.netloc: continue
            link_count+=1
            destination=(path.parent/unquote(parsed.path)).resolve() if parsed.path else path
            if not destination.is_relative_to(ROOT) or not destination.is_file():
                errors.append(f'Missing local link: {path.relative_to(ROOT)} -> {target}')
            elif parsed.fragment and destination.suffix.lower()=='.md':
                if unquote(parsed.fragment) not in anchors(destination.read_text(encoding='utf-8')):
                    errors.append(f'Missing anchor: {path.relative_to(ROOT)} -> {target}')
    milestone=(ROOT/'learning/MILESTONES.md').read_text(encoding='utf-8')
    blocks=re.split(r'(?m)^## M(\d{2}) — ',milestone)
    ids=[int(blocks[i]) for i in range(1,len(blocks),2)]
    if ids!=list(range(1,31)): errors.append('Milestone IDs not exactly M01-M30')
    for i in range(1,len(blocks),2):
        number=int(blocks[i]); block=blocks[i+1]
        for field in ['**Phase:**','**Central question:**','**Understanding target:**',
                      '**Dependencies:**','**Connection and story role:**','**Sources:**']:
            if field not in block: errors.append(f'M{number:02} lacks {field}')
        expected='Background / preliminaries' if number<=12 else 'Narrative / innovation'
        if f'**Phase:** {expected}.' not in block: errors.append(f'Wrong phase M{number:02}')
        dep=re.search(r'\*\*Dependencies:\*\*([^\n]*)',block)
        if dep:
            for m in re.findall(r'\[M(\d{2})\]',dep.group(1)):
                if not 1<=int(m)<number: errors.append(f'Non-earlier dependency M{number:02} -> M{m}')
    if errors: raise AssertionError('\n'.join(errors))
    return {'status':'pass','markdown_pages':len(md),'local_links':link_count,
            'source_math_expressions':formula_count,'milestones':30,'phase_split':[12,18],
            'scope':'Source/navigation only; no hosted rendering claim.'}

if __name__=='__main__': print(json.dumps(run(),indent=2))
