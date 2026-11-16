from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
df = pd.read_csv(ROOT / "data" / "student_performance.csv")
OUT = ROOT / "reports" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

print("Dataset shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nSummary statistics:\n", df.describe(numeric_only=True))
print("\nAverage score by class:\n", df.groupby("Class")["Final_Score"].mean().round(2))
print("\nAverage score by tuition:\n", df.groupby("Extra_Tuition")["Final_Score"].mean().round(2))
print("\nCorrelations:\n", df[["Study_Hours_Per_Day","Attendance_Percent","Final_Score"]].corr().round(2))

plt.figure(figsize=(8,5))
plt.hist(df["Final_Score"], bins=15, edgecolor="black")
plt.title("Distribution of Final Scores"); plt.xlabel("Final Score"); plt.ylabel("Students")
plt.tight_layout(); plt.savefig(OUT/"score_distribution.png", dpi=150); plt.close()

df.groupby("Class")["Final_Score"].mean().reindex(["Class 9","Class 10","Class 11","Class 12"]).plot(kind="bar", figsize=(8,5))
plt.title("Average Score by Class"); plt.ylabel("Average Final Score"); plt.xticks(rotation=0)
plt.tight_layout(); plt.savefig(OUT/"average_score_by_class.png", dpi=150); plt.close()

plt.figure(figsize=(8,5))
plt.scatter(df["Study_Hours_Per_Day"], df["Final_Score"], alpha=.55)
plt.title("Study Hours vs Final Score"); plt.xlabel("Study Hours per Day"); plt.ylabel("Final Score")
plt.tight_layout(); plt.savefig(OUT/"study_hours_vs_score.png", dpi=150); plt.close()
print("\nCharts saved in reports/figures/")
