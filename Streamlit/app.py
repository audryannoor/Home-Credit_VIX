import streamlit as st
import numpy as np
import pandas as pd
import pickle
import scorecardpy as sc
import os
from pathlib import Path

current_directory = Path(__file__).parent #Get current directory
lr_model = open(os.path.join(current_directory, 'logistic regression.pkl'), 'rb')
card = open(os.path.join(current_directory, 'score_card.pkl'), 'rb')
hc_image = open(os.path.join(current_directory, 'hc_image.pkl'), 'rb')
bins = open(os.path.join(current_directory,'bins_woe.pkl'),'rb')

bin_woe = pickle.load(bins)
model = pickle.load(lr_model)
scorecard = pickle.load(card)
image = pickle.load(hc_image)

st.sidebar.image(image)
st.sidebar.title('Credit Score Prediction')
st.sidebar.write("Created By Rafif Noor Audryan")
st.sidebar.write ("[Linkedin] https://www.linkedin.com/in/rafif-noor-audryan/")


NAME = st.text_input('Input Your Name','Anonim')
AGE = st.number_input('Input Your Age',15,100)
CODE_GENDER = st.selectbox('Select Gender: 0 = Female, 1 = Male',[0,1])
NAME_FAMILY_STATUS = st.selectbox('Select Status',['Single / not married','Married','Separated','Widow'])
CNT_CHILDREN = st.number_input('How many Children Your have? Fill 0 If You Dont Have',0)
NAME_EDUCATION_TYPE = st.selectbox('Select Education',['Lower secondary','Secondary / secondary special','Incomplete higher','Higher education','Academic degree'])
NAME_INCOME_TYPE = st.selectbox('Select What Your Income From',['Working','State servant','Commercial associate','Pensioner','Other'])
OCCUPATION_TYPE = st.selectbox('Select What You Occupation',['Office Job','Labour Job','Service Job','Other'])
AMT_INCOME_TOTAL = st.number_input('Input Your Amount Income. Fill 0 If You Dont Have',0)
AMT_ANNUITY = st.number_input('Input Your Amount Annuity. Fill 0 If You Dont Have',0)
AMT_CREDIT = st.slider('Input Amount Credit That You Want. Maximum Credit = 5,000,000',0,5000000)
AMT_GOODS_PRICE = st.slider('Input Amount Goods Price That You Want. Maximum price = 5,000,000',0,5000000)
EMP_LENGTH = st.number_input('How Long Have You Worked, Fill 0 If you not working',0,100)
EXT_SOURCE_1 = st.slider('Input External Source 1 (Normalized score from external data source), Optional',0.0,1.0)
EXT_SOURCE_2 = st.slider('Input external source 2 (Normalized score from external data source), Optional',0.0,1.0)
EXT_SOURCE_3 = st.slider('Input external source 3 (Normalized score from external data source), Optional',0.0,1.0)
FLAG_OWN_CAR = st.selectbox('Have you own car?: 0 = No, 1 = Yes',[0,1])
FLAG_PHONE = st.selectbox('Have you own phone?: 0 = No, 1 = Yes',[0,1])
PHONE_CHANGE_LENGTH = st.number_input('How long was the last phone replacement in year? If dont fill 0',0)
PUBLISH_LENGTH = st.number_input('How long since your credit was last received.If dont fill 0',0)
REGION_POPULATION_RELATIVE = st.slider('Input Region Population Relative, Optional',0.0,1.0)
REGION_RATING_CLIENT = st.slider('Input Region Rating Client, Optional',0,5)
REGIST_LENGTH = st.number_input('Input how long since you registered, Fill 0 if you haven not registered yet',0)

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
    
    X_WOE = sc.woebin_ply(X, bins = bin_woe)
    prediction = model.predict(X_WOE)[0]

    if prediction == 1:
        st.sidebar.error('Credit Application Rejected')
    else:
        st.sidebar.success('Credit Application Approved')


st.button('Predict', on_click = predict)
