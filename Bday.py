import numpy as np
import pandas as pd
import streamlit as st
import time
b = st.empty()
b.title('Binary Classification of Birthdays Using Support Vector Machine')

df = pd.read_csv('countries-aggregated.csv')['Country'].unique()
df = np.delete(df,169)
c = st.container()
with st.form('hi'):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input('Name')
        age = st.number_input('Age',min_value=0,max_value=99,step=1)
        meat = st.selectbox('Whether you eat meat',['Yes','n-Yes 😔'])
    with col2:
        country = st.selectbox("Country you're from",df)
        gender = st.selectbox('Gender',['M','F','Prefer not to say'])
        flavor = st.selectbox('Favorite flavor',['Vanilla','Chocolate'])
    button = st.form_submit_button('Submit')

if button:
    if (gender=='F' and country=='Sri Lanka' and flavor=='Chocolate'):
        for i in range(20):
            st.balloons()
            time.sleep(0.05)
        b.write('')
        c.title('hiiiii')
        c.title('HAPPY BIRTHDAY!!!')
        c.title(f"It's your birthday, {name}!!!")
        c.title(f'You are now {age} years old')
        c.title('your favorite flavor')
        c.title(f'of meat is {flavor}')
        c.title('and ily <3')
    else:
        with st.spinner('Loading...'):
            time.sleep(6)
        st.error('oh no')
        time.sleep(2)
        st.error('an error has occured')
        time.sleep(2)
        st.error('please contact your nearest very good friend for help')




        
