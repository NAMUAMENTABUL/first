import streamlit as st

if st.button('버튼'):
    st.write('너는 병신')
else:
    st.write('안녕하세요!!!')

text_contents = '''다운로드 받은 파일입니다.'''
st.download_button('다운로드', text_contents)

st.subheader('2. radio button test')
food = st.radio(
    "좋아하는 음식은 무엇인가요?",
    ('초밥', '짜장면', '김치볶음밥'))

if food == '초밥':
    st.write('You selected 초밥.')
elif food == '짜장면':
    st.write('You selected 짜장면.')
elif food == '김치볶음밥':
    st.write('You selected 김치볶음밥')

import streamlit as st

st.subheader('1. Checkbox test')
a = st.checkbox('1번')
b = st.checkbox('2번')
c = st.checkbox('3번')

if a:
    st.write('1번을 선택하셨습니다.')
if b:
    st.write('2번을 선택하셨습니다.')
if c:
    st.write('3번을 선택하셨습니다.')







