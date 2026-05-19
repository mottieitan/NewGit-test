import streamlit as st
import pandas as pd
import numpy as np

st.title("דשבורד אינטרקטיבי לדוגמה")

# יצירת נתונים לדוגמה
@st.cache_data
def get_data():
    np.random.seed(42)
    data = pd.DataFrame({
        "תאריך": pd.date_range(start="2023-01-01", periods=100),
        "ערך": np.random.randint(10, 100, 100),
        "קטגוריה": np.random.choice(["A", "B", "C"], 100)
    })
    return data

df = get_data()

# אפשרות לסינון לפי קטגוריה
selected_category = st.selectbox("בחר קטגוריה לסינון", options=df["קטגוריה"].unique(), index=0)

filtered = df[df["קטגוריה"] == selected_category]

st.write(f"הצגת נתונים לקטגוריה: {selected_category}")

st.dataframe(filtered)

st.line_chart(filtered.set_index("תאריך")["ערך"])

st.bar_chart(filtered.groupby("קטגוריה")["ערך"].sum())