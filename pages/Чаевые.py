import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

def fig_to_png(fig):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight', dpi=200)
    buf.seek(0)
    return buf

st.title("Анализ чаевых")
st.sidebar.header("Фильтры")

upload = st.file_uploader("Загрузи tips.csv", type="csv")

if upload is not None:
    tips = pd.read_csv(upload)
    st.write(tips.head())

    days = st.sidebar.multiselect("Дни", tips["day"].unique(), default=tips["day"].unique())
    tips = tips[tips["day"].isin(days)]

    day_sum = tips.groupby("day")["tip"].sum().reindex(["Thur", "Fri", "Sat", "Sun"])
    st.subheader("Сумма чаевых по дням")
    st.bar_chart(day_sum)
    st.download_button("Скачать CSV", day_sum.to_csv(), "day_sum.csv")

    fig, ax = plt.subplots()
    ax.bar(day_sum.index, day_sum.values, color="skyblue", edgecolor="black")
    ax.set_title("Сумма чаевых по дням")
    ax.set_ylabel("Чаевые $")
    st.pyplot(fig)
    st.download_button("Скачать график", fig_to_png(fig), "day_sum.png", "image/png")
    plt.close(fig)

    sex_avg = tips.groupby("sex")["tip"].mean()
    st.subheader("Чаевые: мужчины vs женщины")
    st.bar_chart(sex_avg)
    st.download_button("Скачать CSV", sex_avg.to_csv(), "sex_avg.csv")

    st.subheader("Чаевые от суммы счёта")
    fig2, ax2 = plt.subplots()
    ax2.scatter(tips["total_bill"], tips["tip"], color="coral", alpha=0.7)
    ax2.set_xlabel("Счёт $")
    ax2.set_ylabel("Чаевые $")
    st.pyplot(fig2)
    st.download_button("Скачать график", fig_to_png(fig2), "scatter.png", "image/png")
    plt.close(fig2)

else:
    st.info("Загрузи файл tips.csv")