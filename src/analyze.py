from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parents[1]
out = root / "results"
out.mkdir(exist_ok=True)
d = pd.read_csv(root / "data/departments_2026.csv")
a = pd.read_csv(root / "data/selected_age_groups.csv")
assert len(d) == 7 and d.department.is_unique
assert (d[["female", "male"]] >= 0).all().all()
d["total"] = d.female + d.male
d["share_pct"] = 100 * d.total / d.total.sum()
a["absolute_change"] = a["2035"] - a["2026"]
a["change_pct"] = 100 * a.absolute_change / a["2026"]
d.to_csv(out / "department_summary.csv", index=False)
a.to_csv(out / "age_group_change.csv", index=False)
ax = d.sort_values("total").plot.barh(x="department", y=["female","male"], stacked=True, figsize=(9,5))
ax.set(xlabel="Projected population", title="Santa Cruz: population by department, 2026")
ax.figure.tight_layout()
ax.figure.savefig(out / "departments.png", dpi=160)
plt.close(ax.figure)
ax = a.plot.bar(x="age_group", y=["2026","2035"], figsize=(9,5), rot=0)
ax.set(ylabel="Projected population", title="Selected age groups: 2026 vs 2035")
ax.figure.tight_layout()
ax.figure.savefig(out / "age_groups.png", dpi=160)
plt.close(ax.figure)
print(d.to_string(index=False))
print(a.to_string(index=False))
