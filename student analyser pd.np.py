import numpy as np
import pandas as pd

# ==========================================
# 📌 Initial Dataset Setup
# ==========================================
df = pd.DataFrame({
    "Name": ["Vishali", "Arun", "Priya", "Kumar", "Anitha", "Rahul", "Priya"],
    "Department": ["AI", "CSE", "AI", "AI", "CSE", "AI", "AI"],
    "Python": [85, 72, 91, np.nan, 67, 78, 91],
    "ML": [90, 65, 95, 42, 74, np.nan, 95],
    "Study_Hours": [4, 3, 5, 1, 3, 2, 5]
})

print("--- Initial Raw DataFrame ---")
print(df)


# ==========================================
# 🧩 Task 1 — Inspect the Dataset
# ==========================================
print("\n--- Task 1: Dataset Info ---")
df.info()

print("\n--- Task 1: Dataset Summary ---")
print(df.describe())


# ==========================================
# 🧩 Task 2 & 3 — Handle Missing Values
# ==========================================
print("\n--- Task 2: Missing Values Count ---")
print(df.isna().sum())

# Calculate means using NumPy
python_mean = np.nanmean(df["Python"])
ml_mean = np.nanmean(df["ML"])

# Fill missing values
df["Python"] = df["Python"].fillna(python_mean)
df["ML"] = df["ML"].fillna(ml_mean)


# ==========================================
# 🧩 Task 4 — Remove Duplicates
# ==========================================
print("\n--- Task 4: Duplicate Check ---")
print(df.duplicated())

# Drop duplicate rows
df = df.drop_duplicates().reset_index(drop=True)


# ==========================================
# 🧩 Tasks 5–9 — Feature Engineering
# ==========================================
# Task 5: Total Marks
df["Total"] = df["Python"] + df["ML"]

# Task 6: Average Marks (Rounded to 2 decimal places)
df["Average"] = np.round(df["Total"] / 2, 2)

# Task 7: Result Column
df["Result"] = np.where(df["Average"] >= 50, "Pass", "Fail")

# Task 8: Performance Column
df["Performance"] = np.where(
    df["Average"] >= 80, "Excellent",
    np.where(df["Average"] >= 60, "Good", "Needs Improvement")
)

# Task 9: Study Level Column
df["Study_Level"] = np.where(
    df["Study_Hours"] >= 4, "High",
    np.where(df["Study_Hours"] >= 2, "Medium", "Low")
)


# ==========================================
# 🎯 Final Clean DataFrame
# ==========================================
print("\n--- Cleaned & Transformed DataFrame ---")
print(df)


# ==========================================
# 🧩 Task 10 — Dataset Analysis
# ==========================================
print("\n--- Task 10: Data Analysis ---")

# 1. Average Python Mark
avg_python = np.round(df["Python"].mean(), 2)
print(f"1. Average Python Mark: {avg_python}")

# 2. Average ML Mark
avg_ml = np.round(df["ML"].mean(), 2)
print(f"2. Average ML Mark: {avg_ml}")

# 3. Highest Python Mark
highest_python = df["Python"].max()
print(f"3. Highest Python Mark: {highest_python}")

# 4. Highest ML Mark
highest_ml = df["ML"].max()
print(f"4. Highest ML Mark: {highest_ml}")

# 5. Highest Scorer (Who has the highest total)
top_scorer = df.loc[df["Total"].idxmax(), "Name"]
highest_total = df["Total"].max()
print(f"5. Highest Scorer: {top_scorer} (Total: {highest_total})")


# ==========================================
# 🏆 BONUS — Department-wise Analysis
# ==========================================
print("\n--- Bonus: Department-wise Analysis ---")

dept_analysis = df.groupby("Department")[["Python", "ML", "Total", "Average"]].mean().round(2)
print(depart_analysis)