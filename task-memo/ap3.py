import streamlit as st

login_page = st.container()
sign_up_page = st.container()
main_page = st.container()
sign_btn = st.container()
sign_up = st.container()

if 'loggedIn' not in st.session_state:
    st.session_state['loggedIn'] = False

with sign_btn:
    su = st.button("sign up", key="sign up")

with sign_up:
    si = st.button("login", key="login")

if si:
    sign_btn.empty()
    with login_page:
        st.text("login")
        user_name = st.text_input("user name", "enter your user name")
        password = st.text_input("password", "enter your password", type="password")
        st.button("login", key="login_1")
        #st.write(user_name)
        #st.write(password)
        st.session_state['loggedIn'] = True

        st.write(st.session_state['loggedIn'])
        
        #sign_up.empty()



if su:

    if st.session_state['loggedIn'] == False:
        with sign_up_page:
            st.text("sign up")
            user_name = st.text_input("user name", "enter your user name")
            password = st.text_input("password", "enter your password", type="password")
            st.button("sign up", key="sign_up_1")
            #st.write(user_name)
            #st.write(password)
            st.session_state['loggedIn'] = True

            st.write(st.session_state['loggedIn'])

    else:
        st.write("you are already logged in")




#st.write(st.session_state['loggedIn'])