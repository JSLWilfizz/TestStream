import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Exploratory Data Analysis App')

uploaded_file = st.file_uploader('Upload a CSV file', type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader('Data Preview')
    st.write(df.head())

    st.subheader('Summary Statistics')
    st.write(df.describe())

    columns = df.select_dtypes(include=['float', 'int']).columns
    if len(columns) > 0:
        column = st.selectbox('Select column for histogram', columns)
        fig, ax = plt.subplots()
        df[column].hist(ax=ax, bins=30)
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency')
        st.pyplot(fig)
    else:
        st.write('No numeric columns available for histogram.')
else:
    st.write('Please upload a CSV file to begin.')
