import streamlit as st
import numpy as np
import pandas as pd
import joblib
import pickle
import scorecardpy as sc
from PIL import Image
image = Image.open('https://github.com/audryannoor/Home-Credit_VIX/blob/0b41d8d20622467e82cca8205682035130ca5c3a/Streamlit/hc.png')

model = joblib.load("logistic regression.joblib")
scorecard = pickle.load(open("scorecard.pickle", "rb"))

st.sidebar.image(image)
st.sidebar.title('Credit Score Prediction')
st.sidebar.write("Created By Rafif Noor Audryan")
st.sidebar.write ("Linkedin: https://www.linkedin.com/in/rafif-noor-audryan/")
NAME = st.text_input('Input your name','Anonim')
AGE = st.number_input('Input your age',0,100)
CODE_GENDER = st.selectbox('Select gender: 0 = Female, 1 = Male',[0,1])
NAME_FAMILY_STATUS = st.selectbox('Select status',['Single / not married','Married','Separated','Widow'])
CNT_CHILDREN = st.number_input('How many children you have.Fill 0 if you dont have',0)
NAME_EDUCATION_TYPE = st.selectbox('Select education',['Lower secondary','Secondary / secondary special','Incomplete higher','Higher education','Academic degree'])
NAME_INCOME_TYPE = st.selectbox('Select what you income from',['Working','State servant','Commercial associate','Pensioner','Other'])
OCCUPATION_TYPE = st.selectbox('Select what you occupation',['Office Job','Labour Job','Service Job','Other'])
AMT_INCOME_TOTAL = st.number_input('Input your amount income.Fill 0 if you dont have',0)
AMT_ANNUITY = st.number_input('Input your amount annuity.Fill 0 if you dont have',0)
AMT_CREDIT = st.slider('Input amount credit that you want.Maximum credit = 5,000,000',0,5000000)
AMT_GOODS_PRICE = st.slider('Input amount goods price that you want.Maximum price = 5,000,000',0,5000000)
EMP_LENGTH = st.number_input('Input your employment length',0,100)
EXT_SOURCE_1 = st.slider('Input external source 1',0.0,1.0)
EXT_SOURCE_2 = st.slider('Input external source 2',0.0,1.0)
EXT_SOURCE_3 = st.slider('Input external source 3',0.0,1.0)
FLAG_OWN_CAR = st.selectbox('Have you own car?: 0 = No, 1 = Yes',[0,1])
FLAG_PHONE = st.selectbox('Have you own phone?: 0 = No, 1 = Yes',[0,1])
PHONE_CHANGE_LENGTH = st.number_input('Input your last phone change.If dont fill 0',0)
PUBLISH_LENGTH = st.number_input('Input your last publish.If dont fill 0',0)
REGION_POPULATION_RELATIVE = st.slider('Input REGION_POPULATION_RELATIVE',0.0,1.0)
REGION_RATING_CLIENT = st.slider('Input REGION_RATING_CLIENT',0,5)
REGIST_LENGTH = st.number_input('Input REGIST_LENGTH',0)

def predict():
    X = pd.DataFrame({'AGE':AGE,
                 'AMT_ANNUITY' :AMT_ANNUITY,
                  'AMT_CREDIT':AMT_CREDIT,
                  'AMT_GOODS_PRICE':AMT_GOODS_PRICE,
                  'AMT_INCOME_TOTAL': AMT_INCOME_TOTAL,
                  'CNT_CHILDREN':CNT_CHILDREN,
                  'CODE_GENDER':CODE_GENDER,
                  'EMP_LENGTH':EMP_LENGTH,
                  'EXT_SOURCE_1':EXT_SOURCE_1,
                  'EXT_SOURCE_2':EXT_SOURCE_2,
                  'EXT_SOURCE_3':EXT_SOURCE_3,
                  'FLAG_OWN_CAR':FLAG_OWN_CAR,
                  'FLAG_PHONE':FLAG_PHONE,
                  'NAME_EDUCATION_TYPE': NAME_EDUCATION_TYPE,
                  'NAME_FAMILY_STATUS': NAME_FAMILY_STATUS,
                  'NAME_INCOME_TYPE': NAME_INCOME_TYPE,
                  'OCCUPATION_TYPE': OCCUPATION_TYPE,
                  'PHONE_CHANGE_LENGTH':PHONE_CHANGE_LENGTH,
                  'PUBLISH_LENGTH':PUBLISH_LENGTH,
                  'REGION_POPULATION_RELATIVE':REGION_POPULATION_RELATIVE,
                  'REGION_RATING_CLIENT':REGION_RATING_CLIENT,
                  'REGIST_LENGTH':REGIST_LENGTH},index=[0])
    credit_score = sc.scorecard_ply(X, scorecard, print_step=0)
    result = credit_score.iloc[0,0]
    st.sidebar.write(NAME,"Your Credit Score",result)
    
    if result < 500:
        st.sidebar.error("Credit Application Rejected")
    else:
        st.sidebar.success("Credit application Approved")

st.button('Predict', on_click = predict)
