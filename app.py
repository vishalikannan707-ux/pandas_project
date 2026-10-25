
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Marks Analyser",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Student Marks Analyser")
st.write("Explore student performance using Python and Pandas.")

# Sample dataset based on your existing project
data = {
    "Name": [
        "Vishali", "Arun", "Priya", "Kumar",
        "Anitha", "Rahul", "Meena", "Karthik"
    ],
    "Department": [
        "AI", "CSE", "AI", "AI",
        "CSE", "ECE", "CSE", "AI"
    ],
    "Math": [90, 80, 95, 70, 85, 75, 88, 92],
    "Science": [85, 75, 90, 65, 80, 78, 84, 89],
    "Attendance": [95, 88, 92, 76, 85, 80, 90, 94]
}

df = pd.DataFrame(data)

# Optional CSV upload
uploaded_file = st.file_uploader(
    "Upload a student CSV file (optional)",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        required = [
            "Name", "Department", "Math",
            "Science", "Attendance"
        ]
        missing = [col for col in required if col not in df.columns]

        if missing:
            st.error("Missing required columns: " + ", ".join(missing))
            st.stop()

        for col in ["Math", "Science", "Attendance"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        df = df.dropna(subset=["Math", "Science", "Attendance"])

    except Exception as e:
        st.error(f"Could not read this CSV: {e}")
        st.stop()

# Calculate student performance
df["Average"] = df[["Math", "Science"]].mean(axis=1)

def performance(avg):
    if avg >= 90:
        return "Excellent"
    elif avg >= 80:
        return "Good"
    elif avg >= 70:
        return "Average"
    return "Needs Improvement"

df["Performance"] = df["Average"].apply(performance)

if df.empty:
    st.warning("No student records are available to analyse.")
    st.stop()

# Sidebar filters
st.sidebar.header("Filter students")

departments = sorted(df["Department"].dropna().unique().tolist())
selected = st.sidebar.multiselect(
    "Department",
    departments,
    default=departments
)

min_marks = st.sidebar.slider(
    "Minimum average marks",
    min_value=0,
    max_value=100,
    value=0
)

filtered = df[
    df["Department"].isin(selected)
    & (df["Average"] >= min_marks)
]

# Dashboard metrics
c1, c2, c3 = st.columns(3)

c1.metric("Students", len(filtered))
c2.metric(
    "Average marks",
    f"{filtered['Average'].mean():.2f}"
    if not filtered.empty else "N/A"
)
c3.metric(
    "Highest average",
    f"{filtered['Average'].max():.2f}"
    if not filtered.empty else "N/A"
)

st.subheader("👩‍🎓 Student Records")
st.dataframe(filtered, use_container_width=True)

st.subheader("📈 Average Marks by Department")

if not filtered.empty:
    dept_avg = (
        filtered.groupby("Department")["Average"]
        .mean()
        .sort_values(ascending=False)
    )
    st.bar_chart(dept_avg)
else:
    st.info("No students match your selected filters.")

st.subheader("🏆 Top Performers")

if not filtered.empty:
    st.dataframe(
        filtered.nlargest(3, "Average")[
            ["Name", "Department", "Average", "Performance"]
        ],
        use_container_width=True
    )

st.caption(
    "Built with Python, Pandas and Streamlit | Skillory Space"
)
