import pandas as pd

data = {
    "Name": ["Vishali", "Arun", "Priya", "Kumar", "Anitha", "Rahul", "Meena", "Karthik"],
    "Age": [19, 20, 18, 21, 19, 22, 20, 19],
    "Department": ["AI", "CSE", "AI", "AI", "CSE", "ECE", "CSE", "AI"],
    "Math": [90, 80, 95, 70, 85, 75, 88, 92],
    "Science": [85, 75, 90, 65, 80, 78, 84, 89],
    "Attendance": [95, 88, 92, 76, 85, 80, 90, 94]
}

df = pd.DataFrame(data)

print(df)
print((df.shape[0]))
print((df.shape[1:3]))
print(df.head(3))
print(df.info())
print(df.describe())
df["Average"] = df.apply(
    lambda row: (row["Math"] + row["Science"]) / 2,
    axis=1
)

def performance(avg):
    if avg >= 90:
        return "Excellent"
    elif avg >= 80:
        return "Good"
    elif avg >= 70:
        return "Average"
    else:
        return "Needs Improvement"

    df["Performance"] = df["Average"].apply(performance)

    df[df["Average"] >= 85]
    df[df["Attendance"] >= 90]
    df[df["Department"] == "AI"]

    df.sort_values("Average", ascending=False)
    df.groupby("Department")["Average"].mean()
    df.groupby("Department")["Average"].max()
    df.groupby("Department")["Average"].min()

    df["Attendance"].mean()
    df["Average"].max()
    df["Average"].min()

    print(df["Department"].value_counts())
    print(df[["Average", "Attendance"]].corr())