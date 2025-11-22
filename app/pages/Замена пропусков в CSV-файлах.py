#Импорт библиотек
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#Название
st.title('Анализ данных от онлайн-школы Эльбрус')

#Описание

st.write('Загрузи CSV файл и заполни пропуски')

#Шаг 1. Загрузка CSV файла

uploaded_file = st.sidebar.file_uploader("Choose a file", type='csv')
try:
    df = pd.read_csv(uploaded_file)
    st.write(df.head(5))
except:
    st.stop()

#Шаг 2. Проверка наличия пропусков в файле

missed_values = df.isna().sum()
missed_values = missed_values[missed_values > 0]
st.write(missed_values)
if len(missed_values)>0:
    fig, ax = plt.subplots()
    sns.barplot(x=missed_values.index, y=missed_values.values)
    ax.set_title('Пропуски в столбцах')
    st.pyplot(fig)
else:
    st.write('Нет пропусков данных')
    st.stop()

#Шаг 3. Заполнить пропуски

if len(missed_values)>0:
    button = st.button('Заполнить пропуски')
    if button:
        df_filled = df[missed_values.index].copy()
        for col in df_filled.columns:
            if df_filled[col].dtype=='object':
                df_filled[col] = df_filled[col].fillna(df_filled[col].mode()[0])
            else:
                df_filled[col] = df_filled[col].fillna(df_filled[col].median())

        st.write(df_filled.head(5))

#Шаг 4. Выгрузить заполненный от пропуской CSV файл
        
        download_button = st.download_button(label="Скачать заполненный CSV файл", 
                   data=df_filled.to_csv(), 
                   file_name='filled_date.csv')