<<<<<<< HEAD
from pkg_resources import require
import streamlit as st
import streamlit_authenticator as sa
from modules import authenticate
from pages import page_2


if 'loggedIn' not in st.session_state:
    st.session_state['loggedIn'] = False




st.sidebar.title("choose your option")
si_op = st.sidebar.selectbox("select your option", ["sign in", "sign up", "memos", "logout"])
#si_op = st.selectbox("select your option", ["sign in", "sign up"])

if si_op == "sign in" and st.session_state['loggedIn'] == False:


    st.subheader("sign in")
    em = st.text_input("email", "enter your email")
    pas = st.text_input("password", "enter your password")

    if st.button("sign in"):

        #allow = True
        allow = authenticate.authenticate(em, pas)
    
        if allow:
            st.session_state['loggedIn'] = True
            st.success("sign in successful")

            
        else:
            st.session_state['loggedIn'] = False
            st.error("sign in failed")
                

    


elif si_op == "sign up" and st.session_state['loggedIn'] == False:

    st.subheader("sign up")
    
    ema = st.text_input("email", "enter your email")
    pas =st.text_input("password", "enter your password")
    cnp = st.text_input("confirm password", "confirm your password")
    nam = st.text_input("name", "enter your name")
    su = st.button("sign up")
    st.write(su)

    if su:
        if pas == cnp:
            #authenticate.signup(nam, ema, pas)
            st.success("sign up successful")
            st.session_state['loggedIn'] = True
        else:
            st.error("passwords do not match")
            st.session_state['loggedIn'] = False


elif si_op == "memos" and st.session_state['loggedIn'] == True:

    st.subheader("memos")
    st.text("memos")
    #st.write(sg_in)
    if st.session_state['loggedIn'] == True:
        st.text("memos")
        #st.write(sg_in)
        page_2.show_wid(st.session_state['loggedIn'])
    else:
        st.error("please sign in")
        st.write(st.session_state['loggedIn'])



elif si_op == "memos" and st.session_state['loggedIn'] == False:

    st.error("please sign in")
    st.write(st.session_state['loggedIn'])


elif si_op == "logout" and st.session_state['loggedIn'] == True:

        st.subheader("logout")
        lo = st.button('clock to logout')
        if lo:
            st.text("logging out")
            #st.write(sg_in)
            st.session_state['loggedIn'] = False
        else:
            st.error("please sign in")
           # st.write(sg_in)

elif si_op == "logout" and st.session_state['loggedIn'] == False:

    st.error("please sign in")
    #st.write(sg_in)



st.write(st.session_state['loggedIn'])
    





=======
from pkg_resources import require
import streamlit as st
import streamlit_authenticator as sa
from modules import authenticate
from pages import page_2


if 'loggedIn' not in st.session_state:
    st.session_state['loggedIn'] = False




st.sidebar.title("choose your option")
si_op = st.sidebar.selectbox("select your option", ["sign in", "sign up", "memos", "logout"])
#si_op = st.selectbox("select your option", ["sign in", "sign up"])

if si_op == "sign in" and st.session_state['loggedIn'] == False:


    st.subheader("sign in")
    em = st.text_input("email", "enter your email")
    pas = st.text_input("password", "enter your password")

    if st.button("sign in"):

        #allow = True
        allow = authenticate.authenticate(em, pas)
    
        if allow:
            st.session_state['loggedIn'] = True
            st.success("sign in successful")

            
        else:
            st.session_state['loggedIn'] = False
            st.error("sign in failed")
                

    


elif si_op == "sign up" and st.session_state['loggedIn'] == False:

    st.subheader("sign up")
    
    ema = st.text_input("email", "enter your email")
    pas =st.text_input("password", "enter your password")
    cnp = st.text_input("confirm password", "confirm your password")
    nam = st.text_input("name", "enter your name")
    su = st.button("sign up")
    st.write(su)

    if su:
        if pas == cnp:
            #authenticate.signup(nam, ema, pas)
            st.success("sign up successful")
            st.session_state['loggedIn'] = True
        else:
            st.error("passwords do not match")
            st.session_state['loggedIn'] = False


elif si_op == "memos" and st.session_state['loggedIn'] == True:

    st.subheader("memos")
    st.text("memos")
    #st.write(sg_in)
    if st.session_state['loggedIn'] == True:
        st.text("memos")
        #st.write(sg_in)
        page_2.show_wid(st.session_state['loggedIn'])
    else:
        st.error("please sign in")
        st.write(st.session_state['loggedIn'])



elif si_op == "memos" and st.session_state['loggedIn'] == False:

    st.error("please sign in")
    st.write(st.session_state['loggedIn'])


elif si_op == "logout" and st.session_state['loggedIn'] == True:

        st.subheader("logout")
        lo = st.button('clock to logout')
        if lo:
            st.text("logging out")
            #st.write(sg_in)
            st.session_state['loggedIn'] = False
        else:
            st.error("please sign in")
           # st.write(sg_in)

elif si_op == "logout" and st.session_state['loggedIn'] == False:

    st.error("please sign in")
    #st.write(sg_in)



st.write(st.session_state['loggedIn'])
    





>>>>>>> 7b48bb25bf62c2fba2f472759e064bb293e7f20f
