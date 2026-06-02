# AI Prompts and Code Notes

## Prompts Used

### Prompt 1: Scope Selection

```
You are doing a DeepThought Federer-company assignment. Pick one Indian city hub and one or two assignment-approved segments where 25 mid-sized B2B producers can realistically be found. Prefer clusters with public evidence for revenue, operations, growth, systems maturity and leadership depth. Explain the scope choice and likely risks.
```

### Prompt 2: Candidate Qualification

```
Evaluate this company for the Federer profile.

Company:
City:
Segment:
Sources:

First apply gates:
E1 Producer: pass/fail with evidence.
E2 Accessible: pass/fail with evidence.

If both pass, score:
C3 Differentiation out of 20
C4 Decision-maker quality out of 15
C5 Growing sector out of 15
C6 Growth signals out of 15
C7 Systems maturity out of 20
C8 Leadership succession out of 15

Return the score, band, caveats and a one-sentence personalization hook that mentions a real product/facility/certification/growth signal.
```

### Prompt 3: Personalization Hook

```
Write a founder-outreach opening sentence for this company. It must be specific, non-generic and based only on verified evidence below. Avoid saying "I saw your website". Mention the product capability or growth move that would matter to an operator-founder.

Evidence:
```

### Prompt 4: QC Review

```
Audit this shortlist for likely DeepThought rejection risks:
- revenue above Rs 500Cr
- below Rs 50Cr
- foreign/large-group subsidiary
- trader/distributor
- only sales office in chosen city
- no systems maturity evidence
- generic commodity product

Return rows to remove, rows to verify, and rows that are strong passes.
```

## Code Notes

The script `scripts/build_outputs.mjs` stores the structured research rows, computes the Federer score and band, and generates:

- `data/federer_companies_pune.csv`
- `data/candidate_audit_log.csv`
- `data/score_summary.json`
- `data/federer_companies_pune.xlsx`

The script `scripts/score_validator.py` checks:

- 25 rows exist
- C3-C8 sum matches `federer_score`
- band matches score thresholds
- C7 is not zero
- E1/E2 gates are not failed

## Manual Research Choices

AI was used as a structuring and scoring assistant, not as a single source of truth. Each row uses source URLs from official websites, annual reports, market-data pages, rating notes or company databases. Weak evidence is explicitly flagged in the `caveats_next_verification` column rather than hidden.
