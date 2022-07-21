import streamlit as st
import sqlite3
import pandas as pd
import os.path

con = sqlite3.connect('db.db')
cur = con.cursor()

def login_user(id, pw):
    cur.execute(f"SELECT * FROM users WHERE id='{id}' and pwd = '{pw}'")
    return cur.fetchone()

menu = st.sidebar.selectbox('MENU', options=['로그인','회원가입','회원목록'])

if menu == '로그인':
    st.subheader('로그인')
    login_id = st.text_input('아이디', placeholder='아이디를 입력하세요')
    login_pw = st.text_input('비밀번호',
                             placeholder='비밀번호를 입력하세요',
                             type='password')
    login_btn = st.button('로그인')
    if login_btn:
        user_info = login_user(login_id, login_pw)
        file_name = './ing/'+user_info[0]+'.jpg'

        if os.path.exists(file_name):
            st.sidebar.image(file_name)
            st.write(user_info[4], '님 환영합니다.')
        else:
            st.write(user_info[4], '님 환영합니다.')

    st.sidebar.subheader('로그인')
if menu == '회원가입':
    st.subheader('회원가입')


    st.info('다음 양식을 모두 입력 후 제출합니다.')
    in_id = st.text_input('아이디', max_chars=12)
    in_name = st.text_input('성명', max_chars=10)
    in_pwd = st.text_input('비밀번호', type='password')
    in_pwd_chk = st.text_input('비밀번호 확인', type='password')
    in_age = st.text_input('나이')
    in_gender = st.radio('성별', options=['남', '여','트렌스 젠더'], horizontal=True)

    in_btn = st.button('회원가입')
    if in_btn:
        if in_pwd != in_pwd_chk:
            st.warning('비밀번호가 일치하지 않습니다.')
            st.stop()
        cur.execute(f"INSERT INTO users(id, pwd, name, age, gender) VALUES ("
                    f"'{in_id}', '{in_pwd}', '{in_name}',{in_age}, '{in_gender}')")
        st.success('회원가입에 성공했습니다.')

        con.commit()



if menu == '회원목록':
    st.subheader('회원목록')
    df = pd.read_sql('SELECT name,age,gender FROM users ', con)
    st.dataframe(df)
    st.sidebar.subheader('회원목록')

    st.video('https://www.youtube.com/watch?v=kBedTDfk4vk')










