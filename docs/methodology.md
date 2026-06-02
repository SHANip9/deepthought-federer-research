# Methodology: Pune Federer Company Research

Prepared for: Souradeep Ghosh

## Scope Chosen

City hub: Pune operational hub, including Chakan, Bhosari, Pimpri-Chinchwad, Sanaswadi, Pirangut, Shirwal and nearby Pune industrial belt where the company has a real plant, R&D centre, manufacturing unit or decision hub.

Segments:

- Industrial sensors & instrumentation
- Precision auto components & engineering

Reason: Pune has a dense B2B manufacturing cluster with automotive OEM suppliers, machine-tool builders, instrumentation makers, metrology companies and automation equipment firms. This gives enough companies in the Rs 50Cr-500Cr revenue band while keeping the research operationally coherent.

## Source Hierarchy

1. Official company website, brochures and annual reports for products, facilities, certifications, leadership and R&D evidence.
2. Public filings and market-data sources for listed-company revenue: BSE/NSE filings, annual reports, StockAnalysis, Groww, Equitymaster and ETMoney.
3. Private-company financial databases for revenue bands and active status: Tofler, The Company Check, EMIS, Growjo and similar profile sources.
4. Credit-rating notes from CARE/CRISIL/ICRA where available because they often show bank facilities, revenue movements and systems maturity.
5. Trade directories and expo materials only as supporting evidence, not primary proof.

## Filtering Process

I applied two eligibility gates before scoring:

- E1 Producer: The company must manufacture a product or deliver an in-house specialized technical service. Pure traders, distributors, importers and sales offices were rejected.
- E2 Accessible: The company must have Indian HQ/primary operations and a real Pune-region operational presence.

After that, I scored C3-C8 exactly against the assignment rubric:

- C3 Differentiation: 0, 10 or 20
- C4 Decision-maker quality: 0, 7.5 or 15
- C5 Growing sector: 0, 7.5 or 15
- C6 Growth signals: 0, 7.5 or 15
- C7 Systems maturity: 0, 10 or 20. A zero here is an automatic fail.
- C8 Leadership succession: 0, 7.5 or 15

Banding:

- 80-100: A, strong Federer
- 60-79: B, probable Federer
- 40-59: C, borderline
- Below 40: D, not ICP

## Growth Signals Used

I counted a company as actively growing when at least two of these were visible:

- Recent revenue growth or current revenue filings
- New facility, automated line, capex or capacity expansion
- Current website, news or investor releases
- Regulatory/quality certification or updated accreditation
- Hiring, new product launches, export expansion or new market entry

## Systems Maturity Evidence

Because many private Indian manufacturing companies do not publish ERP/SAP usage, I did not treat missing ERP screenshots as automatic failure. I accepted the following as moderate-to-strong C7 evidence:

- Explicit ERP/SAP/digital operations references
- IATF 16949, ISO 9001/14001, AS9100, PED, API, ASME or equivalent process-heavy certifications
- Automated production lines with PLC/HMI/SMT/verification loops
- Credit-rating/public-company internal-control evidence
- DSIR-recognized R&D, in-house testing labs and structured validation systems

## Important Caveats

This is a strong submission-ready working set, but before sending outreach I would verify three items:

- Minilec: product fit is strong, but revenue proof is weaker than the other 24. Replace it if MCA/Tofler confirms it below Rs 50Cr.
- Kinetic Engineering: Pune is a real decision hub, but its main manufacturing plant is in Ahilyanagar. Keep it only if DeepThought accepts Pune-hub logic.
- Labindia: verify whether enough revenue comes from owned instrumentation/product capability rather than distribution/service.

## Rejection Logic

I kept an audit log in `data/candidate_audit_log.csv`. Examples rejected:

- Large companies above the Rs 500Cr cutoff: Bharat Forge, Praj, Thermax, Varroc, Endurance, Forbes Marshall.
- Foreign subsidiaries / large-group subsidiaries: WIKA, Nord, Vishay, Benteler, ElringKlinger, Manas Microsystems, Krohne Marshall.
- Traders or distributors: Tronsoft, Duro Technical Systems.
- Great product fit but weak revenue scale: Jayashree Electron, Protocontrol.

## Output Files

- `data/federer_companies_pune.csv`
- `data/federer_companies_pune.xlsx`
- `data/candidate_audit_log.csv`
- `docs/part_b_sourcing_strategy_and_1000_company_proposal.md`
- `docs/ai_prompts_and_code_notes.md`
- `scripts/build_outputs.mjs`
- `scripts/score_validator.py`
