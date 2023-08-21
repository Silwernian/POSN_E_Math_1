import streamlit as st

from streamlit_extras.switch_page_button import switch_page



st.set_page_config(page_title='Mathematics I', page_icon=':root:')


st.header('Welcome to :violet[**Mathematics I**]')
st.caption('by :violet[**Physics Meerkat**]')
st.divider()

st.subheader(':blue[**Topics**]')

Lecture = [':blue[**Functions**] and their :blue[**Derivatives**]']
pages_name = ['Derivatives of a function']
switch_button = []
col = st.columns([1,1])
for i in range(len(Lecture)):
    switch_button.append(col[0].button(label='**{}: {}**'.format(i+1,Lecture[i]),use_container_width=True))
    
    if switch_button[i]:
        switch_page(pages_name[i])

st.divider()

