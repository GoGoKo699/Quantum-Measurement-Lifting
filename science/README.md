# Scientific account

A measurement's outcome probabilities and its quantum output are different resources. The [model](model.md) fixes an outcome-only black box and asks for a prescribed quantum instrument on one arbitrary data input. It also fixes the successful map before normalization, so postselection cannot conceal input dependence.

The [construction](construction.md) distributes the data coherently among query ports. A known antisymmetric state occupies the other ports and the retained output. After all destructive calls, a filter on the routing control combines positions with the same reported label. A cofactor identity makes every hidden measurement history either vanish or act as the whole desired projector. Summing successful histories gives one coefficient for the complete instrument, including degenerate sectors.

The [converse](converse.md) uses a different property of destructive access. Each resolved call contributes only an unknown measurement bra. A successful fine-history Kraus matrix is therefore polynomial in conjugated basis entries. Exactness forces that matrix onto a single projector ray. Complexifying this equality makes a determinant factor unavoidable, and its degree requires at least as many calls as the Hilbert-space dimension.

The [boundaries](boundaries.md) explain why full-rank unsharp effects change the exact question, why conditional success is not repeat-until-success, and what workspace and known controls cost. The [worked examples](../learning/WORKED_EXAMPLE.md) make the distinction between quantum coherence and correct classical statistics concrete. The [source comparison](../references/RELATED_WORK.md) credits antisymmetric transformations and general channel-processing tools without importing their stronger oracle access.

**Result ownership:** the model owns theorem statements and conventions; construction owns normalization and achievability; converse owns the universal lower bound; boundaries owns physical restrictions and the full-rank obstruction. The learning files explain these same results rather than defining a second scientific version.
