import streamlit as st

 
headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()
signup = st.container()


def show_signup_page():
    with signup:
        st.text("Sign Up")
        ema = st.text_input("email", "enter your email")
        pas =st.text_input("password", "enter your password")
        cnp = st.text_input("confirm password", "confirm your password")
        nam = st.text_input("name", "enter your name")
        su = st.button("sign up")
        st.write(su)
 
def show_main_page():
    with mainSection:
        dataFile = st.text_input("Enter your Test file name: ")
        Topics = st.text_input("Enter your Model Name: ")
        ModelVersion = st.text_input("Enter your Model Version: ")
        processingClicked = st.button ("Start Processing", key="processing")
        if processingClicked:
               st.balloons() 
 
def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    
def show_logout_page():
    loginSection.empty();
    with logOutSection:
        st.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)
    
def LoggedIn_Clicked(userName, password):
    # call athenticate.login()
    if 1:
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False;
        st.error("Invalid user name or password")
    
def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            userName = st.text_input (label="", value="", placeholder="Enter your user name")
            password = st.text_input (label="", value="",placeholder="Enter password", type="password")
            st.button ("Login", on_click=LoggedIn_Clicked, args= (userName, password))
            #st.button ("Sign Up", on_click=show_signup_page)


with headerSection:
    st.title("Streamlit Application")
    #first run will have nothing in session_state
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        #show_login_page()
        show_signup_page()
    else:
        if st.session_state['loggedIn']:
            show_logout_page()    
            show_main_page()  
            
        else:
            show_login_page()

            
           
        