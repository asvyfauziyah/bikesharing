import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

hour_df = pd.read_csv("hour_df.csv")

all_users = hour_df['count'].sum()
registered_users = hour_df['registered'].sum()
unregistered_users = hour_df['casual'].sum()

# membuat sidebar bisa di hide
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# header sidebar
st.sidebar.header('Parameters')

# subheader sidebar
st.sidebar.subheader('Avarage User/day')
avarage_user= st.sidebar.selectbox('Select by', ('days', 'unregister_user', 'register_user'))

st.sidebar.subheader('By Conditions')
condition= st.sidebar.selectbox('select by', ('weather', 'season'))

st.header('Bike Share Users Dashboard')

# baris 1
st.markdown('### Count of user(s)')
col1, col2, col3 = st.columns(3)
col1.metric("All Users", all_users)
col2.metric("Registered Users", registered_users)
col3.metric("Unregistered Users", unregistered_users)

# baris 2
st.markdown('### Avarage Bike Sharing Users 2018-2019')
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=hour_df, x='hour', y='count', hue='weekday', ax=ax)
ax.set(title='Count of bike sharing users during weekdays and weekends')
st.pyplot(fig)

# baris 3
c1, c2 = st.columns(2)
with c1:
    fig, ax = plt.subplots(figsize=(20,5))
    sns.barplot(data=hour_df, x='month', y='count', ax=ax)
    ax.set(title='Count of bike sharing users during different months')
    st.pyplot(fig)
with c2:
    fig, ax = plt.subplots(figsize=(20,5))
    sns.barplot(data=hour_df, x='weekday', y='count', ax=ax)
    ax.set(title='Count of bike sharing users during different day')
    st.pyplot(fig)

# baris 3
st.markdown('#### Bike Sharing Users on Weather & Season Situation')
fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=hour_df, x='hour', y='count', hue='weather', ax=ax)
ax.set(title='Count of bike sharing users during different weathers')
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(20,5))
sns.pointplot(data=hour_df, x='hour', y='count', hue='season', ax=ax)
ax.set(title='Count of bike sharing users during different seasons')
st.pyplot(fig)
