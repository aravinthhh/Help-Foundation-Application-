
import streamlit as st
import numpy as np
import pandas as pd
import joblib 

#Load the Instances that are created

with open('scaler.joblib','rb') as file:
    s = joblib.load(file)

with open('pca_final.joblib','rb') as file:
    pca_final = joblib.load(file)

with open('final_model.joblib','rb') as file:
    kmeans_final= joblib.load(file)

def prediction(input_list):

    scaled_input = s.tranform([input_list])
    pca_input = pca_final.transform(scaled_input)
    output = model.predict(pca_input)[0]

    if output == 0:
        return 'Developing'
    elif output == 1:
        return 'Developed'
    else:
        return 'Under-Development'

def main():

    st.title('HELP NGO FOUNDATION')
    st.subheader('This application will give the status of the Country based on Socio-Economics and Health Factor')

    gdp = st.text_input('Enter the GDP per Population of a Country')
    inc = st.text_input('Enter the Per Capita of the Country')
    imp = st.text_input('Enter the Import in terms of % of GDP')
    exp = st.text_input('Enter the Export in terms of % of GDP')
    inf = st.text_input('Enter the Inflation Rate of the Country (%)')

    helt = st.text_input('Enter the Health Expenditure in terms of % of GDP')
    ch_m = st.text_input('Enter the Number of Death per 1000 births for < 5 years')
    fer = st.text_input('Enter the Average Childern born to a Women in a Country')
    lf = st.text_input('Enter the Average Life Expectancy in a  Country')

    in_data = [ch_m, exp, helt, imp, inc, inf, lf, fer, gdp]

    if st.button('Predict'):
        response = prediction(in_data)
        st.success(response)


if __name__ == '__main__':
    main()
