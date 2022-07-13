

import streamlit as st
from PIL import Image

st.title('WELCOME TO SITMANG B.M.I CALCULATOR APP')

image=Image.open('images.png')

st.sidebar.image(image,caption='BODY MASS INDEX')

st.balloons()
st.sidebar.title('Personal Details')

name = st.sidebar.text_input('Enter Your name', 'Type here...')

    
add_selectbox = st.sidebar.selectbox('What is Your Gender',('Male','Female'))

st.sidebar.date_input('Enter Your Birthday')
Exercise= st.sidebar.selectbox('Do You Exercise?',('Yes','No'))

Hobby = st.sidebar.selectbox('Hobbies:',['Sports','Reading','Travelling','Movies'])
                                        
height = st.number_input('Please Enter Your Height in cms, m,feet :',100,300 )

weight = st.number_input('Please Enter Your Weight in kg,g,lbs :',1 )

check = st.button('Find BMI')
if(check):
    bmi = round(weight/height/height*10000,2)
    st.title(f'Your BMI : {bmi}')
    if(bmi>30):
        st.title('You are Obese.')
    
    elif(bmi>25):
        st.title('you are Overweight.')
    elif(bmi>18.5):
        st.title('You are Normal Weight.')
    else:
        st.title('You are Underweight.')
