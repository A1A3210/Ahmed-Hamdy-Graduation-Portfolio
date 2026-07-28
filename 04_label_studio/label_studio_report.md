# Label Studio Report — Task 4 (Motrjim Capstone)

## 1) NER Entity Distribution (Project A — Legal NER, 18/18 tasks annotated)

| Entity Type | Count |
|---|---|
| ROLE | 26 |
| DATE | 25 |
| ORG | 18 |
| LEGAL_TERM | 16 |
| JURISDICTION | 13 |
| MONEY | 13 |
| COURT | 11 |
| LAW_STATUTE | 11 |
| CASE | 5 |
| PERSON | 5 |
| **Total entities** | **143** |

`Segment-level check` distribution: `clear` = 14 tasks, `ambiguous_boundary` = 3 tasks (Task 1, Task 2, Task 3), `nested_entity` = 1 task (Task 5).

## 2) Prompt Classification Distribution (Project B, 18/18 tasks annotated)

**Quality tier:**

| Tier | Count |
|---|---|
| poor_underspecified | 8 |
| strong_production_ready | 8 |
| self_contradictory | 2 |
| workable_needs_edits | 0 |

**Risk flag:**

| Flag | Count |
|---|---|
| safe | 15 |
| prompt_injection_or_jailbreak | 1 |
| policy_violation_request | 1 |
| high_stakes_quality_lowering | 1 |

**Rating distribution:** 1★ = 10, 4★ = 4, 5★ = 4 (average 2.56/5).

**Most-used techniques:** none_bare_instruction (8), output_format_control (7), role_persona (5), decomposition_steps (4).

## 3) Three Difficult / Ambiguous Cases

1. **Task 1 (DIFC, triple mention):** "DIFC" appears three times in the same passage, playing two distinct roles — twice as `JURISDICTION` (place of incorporation and governing law) and once as part of `COURT` in "DIFC Courts". Resolved via the explicit boundary rule in the config file (COURT takes priority over JURISDICTION for "DIFC Courts"); logged as `ambiguous_boundary`.

2. **Task 3 (Chapter V and the United States):** "Chapter V" is a legislative cross-reference that does not connect directly to the regulation's name within its own span — the link relies on an implicit inference from the paragraph's first sentence, making its classification as `LAW_STATUTE` non-conclusive on its own terms. Separately, "the United States" was tagged `JURISDICTION` because it functions as the legal territory being evaluated for data-protection adequacy under Chapter V, rather than a mere geographic mention. Both calls are documented and logged as `ambiguous_boundary`.

3. **Task 5 (nested jurisdiction inside a case citation):** "State of Maharashtra" matches the JURISDICTION pattern exactly (cf. "State of Kuwait") but appears embedded inside the CASE citation "Dashrath Rupsingh Rathod v State of Maharashtra (2014)". Resolved by keeping the full citation as a single CASE span per the maximal-contiguous-span rule, without double-tagging the embedded jurisdiction; logged as `nested_entity`.

## 4) Inter-Annotator Agreement

Not applicable — annotation was performed solo (single annotator), no second linguist involved. No IAA percentage calculated, per the optional clause in the task instructions.
