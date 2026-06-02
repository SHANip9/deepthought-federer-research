# Part B: Sourcing Strategy and 1000-Company Proposal

## 1. Other Sourcing Methods Across India

I would source Federer companies through layered datasets rather than generic Google searches:

- MCA + Tofler + The Company Check: identify active Indian manufacturing companies, revenue band, directors, charges and filing freshness.
- Credit rating PDFs: CARE, CRISIL, ICRA and India Ratings notes often reveal revenue, plant expansions, capex, debt facilities, customer concentration and operating risks.
- Industry associations: ACMA, MCCIA Pune, IMTMA, AIAI, CII, FICCI, Indian Chemical Council, Pharmexcil, EEPC India, SIATI and regional MSME associations.
- Trade expos: IMTEX, Automation Expo, Auto Expo Components, Pune Machine Tool Expo, ChemSpec India, India Lab Expo, Medical Fair India, CPHI India and PlastIndia.
- Regulatory/certification data: DSIR-recognized R&D units, CDSCO medical-device registrations, USFDA/WHO-GMP/EU-GMP, IATF 16949, AS9100, ISO 13485, ZED certification and Udyam MSME data.
- Export and import signals: export promotion councils, Zauba/import-export data, port shipment records and buyer-supplier databases.
- Hiring and systems signals: LinkedIn, Naukri, company career pages and job posts mentioning ERP, SAP, MIS, plant head, production planning, costing, quality systems or digital transformation.
- Local cluster maps: MIDC directories, GIDC directories, industrial estate association lists and state investment-promotion portals.

## 2. 1000-Company Proposal: One-Month Scale-Up Plan

Goal: build a verified 1000-company Federer pipeline in 30 days with city, segment, score, evidence links and personalization hooks.

### Week 1: Build the Source Universe

- Pick 8-10 city/segment combinations: Pune auto/instrumentation, Ahmedabad chemicals/textiles, Vadodara specialty chemicals, Hyderabad medtech/defence electronics, Coimbatore precision engineering, Chennai medical devices/auto components, Bengaluru sensors/medtech, Surat chemicals/textiles.
- Pull 4000-5000 raw company names from MCA/company databases, association lists, exhibitor lists and credit-rating PDFs.
- Auto-remove obvious rejects: revenue above Rs 500Cr, inactive companies, traders, generic distributors, large-group subsidiaries and companies with no website.
- Output: 2500-3000 preliminarily relevant companies.

### Week 2: Automated Enrichment

- Enrich each company with website, city, plant address, segment, revenue band, directors, certifications, source links, career page, LinkedIn page and recent news.
- Use AI extraction on official websites and rating PDFs to classify E1/E2 and summarize what the company actually makes.
- Run automated red-flag rules: no website, only sales office, no manufacturing language, revenue mismatch, stale filings, no systems evidence.
- Output: 1500-1800 researchable companies.

### Week 3: Scoring and Human QC

- Score C3-C8 using a rules-plus-AI system.
- Human reviewers check every A-band and every uncertain B-band.
- Add personalization hooks only after the company passes E1/E2 and C7.
- Use a 10% sample audit by a second reviewer to catch hallucinated claims, wrong city fit or weak source links.
- Output: 1100-1300 likely Federer companies.

### Week 4: Final Verification and Packaging

- Re-check revenue band and C7 systems maturity for all companies.
- Remove companies with weak evidence, leaving 1000 qualified targets.
- Split output by city, segment, score band and outreach priority.
- Create GitHub/Drive deliverables: master CSV, methodology, prompts, audit log and weekly dashboard.
- Prepare Internshala/chat version with sourcing logic and hand-drawn diagram photo.

## Automation Stack

- Scraping/enrichment: Python requests, Playwright for dynamic pages, Google/Bing programmable search where permitted.
- Parsing: PDF text extraction, structured HTML extraction and regex only for clean known fields.
- AI: classify producer/distributor, summarize product capability, detect growth signals and draft personalization hooks.
- Database: Airtable/Notion/Postgres table with source URLs and confidence scores.
- QC: duplicate checks, source-link validity checks, score recalculation, reviewer sign-off and random audit.

## Quality Control Checkpoints

- Gate QC: every company must pass E1 and E2 before scoring.
- Revenue QC: every included company needs a source or reasoned estimate for Rs 50Cr-500Cr.
- Systems QC: C7 cannot be blank or zero. If no ERP/certification/process evidence exists, remove the company.
- Source QC: every scored claim must map to a source URL.
- Personalization QC: hooks must mention a real product, facility, certification, market move or leadership signal.
- Final QC: at least 10% of the 1000 list rechecked by a second person.

## Hand-Drawn Diagram Instructions

Do not submit a digital diagram. Draw this by hand on paper and send a photo in Internshala chat.

Suggested diagram layout:

Title: "1000 Federer Companies in 30 Days"

Left to right flow:

1. Raw Sources
   MCA, Tofler, associations, expos, rating PDFs, certification lists, job boards
2. Auto Filters
   active, India ops, Rs 50-500Cr, producer, not subsidiary, current website
3. AI Enrichment
   product summary, city proof, growth signals, ERP/systems evidence, leadership
4. Human QC
   E1/E2 gate check, source validation, C7 check, revenue check
5. Federer Score
   C3-C8, Band A/B/C/D, reject D and weak C
6. Output
   1000-company CSV, audit log, methodology, personalized hooks

Draw a feedback loop from Human QC back to Auto Filters labelled "bad patterns update rules".

Draw a weekly timeline below:

- Week 1: 5000 raw to 3000 filtered
- Week 2: 3000 to 1800 enriched
- Week 3: 1800 to 1200 scored
- Week 4: 1200 to 1000 verified

Add one small box at the bottom: "No C7 evidence = automatic fail".
