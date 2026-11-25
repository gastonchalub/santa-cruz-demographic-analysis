# Santa Cruz demographic analysis

Exploratory analysis of population projections for Santa Cruz, Argentina, 2026–2035, developed for regional data storytelling.

## Data

The available tables were reconstructed from earlier project notes, not directly from the original source workbook. They include 2026 projections by sex for all seven departments and selected age groups for 2026 and 2035. The age table is deliberately incomplete and must not be summed as the provincial population. The original source, projection vintage and definitions require verification before formal publication.

The reconstructed departmental total for 2026 is 335,096. These values are projections, not observed census counts.

## Analysis

- Departmental totals and provincial population shares.
- Sex composition by department.
- Absolute and relative change in selected age groups from 2026 to 2035.

## Run

```bash
pip install -r requirements.txt
python src/analyze.py
```

Outputs are written to results/. The original animation and complete projection series were not recovered. This is a partial reconstruction; code has not been rerun as part of publication.
