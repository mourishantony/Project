import streamlit as st

selected = st.selectbox('Select one option:', ['', 'First one', 'Second one'], format_func=lambda x: 'Select an option' if x == '' else x)

if selected:
    st.success('Yay! 🎉')
else:
    st.warning('No option is selected')
