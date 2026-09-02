# Final Project — Data Analyst Capstone Project Report

## Deliverable

`Data Analyst Capstone Project Report.pptx` — 31 slides, built on
`Data Analyst Capstone Template 2026.pptx` (same master, layouts, theme and artwork).

### Remaining step: convert to PDF

This machine has neither PowerPoint nor LibreOffice, so the PDF must be produced
manually. Any of these works:

- **PowerPoint Online / Microsoft 365** — upload to OneDrive, open, then
  `File → Save As → Download as PDF`.
- **Google Slides** — upload to Drive, open with Slides, then
  `File → Download → PDF Document`.
- **LibreOffice** (if installed later):
  `soffice --headless --convert-to pdf "Data Analyst Capstone Project Report.pptx"`

The exported file must be named **`Data Analyst Capstone Project Report`** (`.pdf`).
Submit through **one** option only — AI-graded or peer-graded, never both.

## Slide map

| # | Slide | Contents |
|---|-------|----------|
| 1 | Title | Title, author, date |
| 2 | Outline | Section list |
| 3 | Executive Summary | 7 headline findings |
| 4 | Introduction | Purpose, audience, business questions, value |
| 5 | Methodology | Sources, wrangling steps, tools |
| 6 | Methodology — Data Quality | Missing-value chart + treatment decisions *(added)* |
| 7 | Results | Section divider |
| 8 | Job Postings | Bar chart, descending by postings |
| 9 | Popular Languages | Bar chart, descending by salary |
| 10 | Programming Language Trends | Top 10 current vs. next year |
| 11 | …Findings & Implications | 5 findings, 5 implications |
| 12 | Database Trends | Top 10 current vs. next year |
| 13 | …Findings & Implications | 5 findings, 5 implications |
| 14 | Dashboard | Section divider |
| 15 | Dashboard Tab 1 | Current technology usage + insight |
| 16 | Dashboard Tab 2 | Future technology trends + insight |
| 17 | Dashboard Tab 3 | Demographics + insight |
| 18 | Discussion | Cross-tab synthesis |
| 19 | Overall Findings & Implications | 7 findings, 7 implications |
| 20 | Conclusion | 6 points incl. limitations and next steps |
| 21 | Appendix | Index of A1–A10 |
| 22–31 | A1–A10 | Unused charts + methodology reference table |

A watermark text box sits on the slide master (and every layout, so no layout can
drop it), as the brief permits.

## Reproducing the deck

```bash
python build_charts.py   # regenerates assets/*.png and assets/facts.json
python build_deck.py     # rebuilds the .pptx from the template
python qa_deck.py        # geometry / leftover-placeholder checks
```

`build_charts.py` prints every number quoted on the slides, and `build_deck.py`
reads them from `assets/facts.json`, so the narrative cannot drift from the data.

## Data sources

| Source | Artefact | Used for |
|---|---|---|
| Jobs API | `02-collecting-data-using-apis/job-postings.xlsx`, `skills-job-postings.xlsx` | Slides 8, A3 |
| Web scraping | `04-collecting-data-using-web-scraping/popular-languages.csv` | Slide 9 |
| Stack Overflow survey | `25-building-dashboard-google-locker/survey_data_updated.csv` | Slides 10–20, A1–A10 |

## Analysis notes worth knowing

- **Current vs. desired is normalised, not subtracted.** Respondents name 6.19
  languages they have used but only 5.64 they want (3.69 vs. 3.50 for databases),
  so raw count differences push nearly every technology negative. Slides A1–A2
  compare each side as a share of all selections on its own question, which
  isolates the real change in priority. This is the deck's main analytical
  contribution beyond the labs.
- **Compensation is never imputed.** 49.3% of `ConvertedCompYearly` is missing;
  filling half a column with its own median would manufacture a false peak, so
  pay analysis runs on the 9,550 valid responses and says so on the slide.
- **The `C` job-posting count (25,114) is flagged unreliable** on slides 19 and
  A3 — it is almost certainly inflated by substring matching in job text.
- **Chart colour encodes the time dimension**: purple = current year,
  orange = next year, teal = demographics, red = negative change. The palette was
  validated for colour-vision deficiency (all-pairs CVD ΔE 9.2, normal-vision
  ΔE 27.6 on a white surface).

## Before you export

The layout was verified geometrically (`qa_deck.py`: nothing off-canvas, no
picture/text collisions, no leftover template prompts) but **not visually** — no
renderer was available. Worth a quick eyeball on open:

- [ ] Slides 11, 13, 19 — the two-column findings/implications text is the densest
      in the deck. Autofit is on, so PowerPoint should shrink it; confirm it did.
- [ ] Slides 15–17 — the wide dashboard image sits between the title and the
      insight bullets; check no clipping at the bottom.
- [ ] Slide 31 — the reference table's header row should be readable
      (white bold on the theme's accent fill).
- [ ] Watermark visible at the foot of each slide, not hidden behind artwork.
- [ ] IBM Plex Sans is not installed here, so PowerPoint may substitute a font
      and reflow text slightly.
