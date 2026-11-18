from pathlib import Path

import altair as alt
import joblib
import numpy as np
import pandas as pd
import streamlit as st

LAB_DIR = Path(__file__).resolve().parent
MODEL_PATH = LAB_DIR / "outputs" / "advertising_model.joblib"
LABELS = {"TV": "Телевидение", "radio": "Радио", "newspaper": "Газеты"}

st.set_page_config(page_title="Прогноз продаж Advertising", layout="wide")
st.title("Прогноз продаж Advertising")
st.write("Линейная регрессия по расходам на телевидение, радио и газеты.")

if not MODEL_PATH.is_file():
    st.error("Выполните ноутбук lab3_anaconda.ipynb, чтобы сохранить модель C.")
    st.stop()


@st.cache_resource
def load_model(path, modified_ns):
    return joblib.load(path)


model = load_model(MODEL_PATH, MODEL_PATH.stat().st_mtime_ns)
channels = model.feature_names_in_.tolist()
data = pd.read_csv(LAB_DIR / "data" / "Advertising.csv", usecols=channels)

st.sidebar.header("Рекламный бюджет")
budgets = {}
for channel in channels:
    budgets[channel] = st.sidebar.slider(
        f"{LABELS[channel]}, тыс. долл.",
        min_value=float(data[channel].min()),
        max_value=float(data[channel].max()),
        value=round(float(data[channel].median()), 1),
        step=0.1,
        key=channel,
    )

current = pd.DataFrame([budgets], columns=channels)
prediction = float(model.predict(current)[0])
st.metric("Прогноз продаж", f"{prediction:.2f} тыс. ед.")

axis_channel = st.selectbox("Изменяемый канал на графике", channels, format_func=LABELS.get)
grid = pd.DataFrame({channel: np.full(100, budgets[channel]) for channel in channels})
grid[axis_channel] = np.linspace(data[axis_channel].min(), data[axis_channel].max(), len(grid))
curve = pd.DataFrame({"budget": grid[axis_channel], "sales": model.predict(grid)})
point = pd.DataFrame({"budget": [budgets[axis_channel]], "sales": [prediction]})

encoding = {
    "x": alt.X("budget:Q", title=f"{LABELS[axis_channel]}, тыс. долл.", scale=alt.Scale(zero=False)),
    "y": alt.Y("sales:Q", title="Прогноз продаж, тыс. ед.", scale=alt.Scale(zero=False)),
    "tooltip": [
        alt.Tooltip("budget:Q", title="Бюджет, тыс. долл.", format=".1f"),
        alt.Tooltip("sales:Q", title="Прогноз, тыс. ед.", format=".2f"),
    ],
}
line = alt.Chart(curve).mark_line(color="#216C70").encode(**encoding)
marker = alt.Chart(point).mark_circle(color="#A95020", size=110).encode(**encoding)
st.altair_chart((line + marker).properties(height=320), width="stretch")
st.caption("Точка показывает текущий прогноз. На линии остальные бюджеты фиксированы.")
