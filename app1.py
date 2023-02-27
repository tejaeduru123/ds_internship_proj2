import streamlit as st

st.title("Data Science Intern 2023")
st.header("Eduru Teja")


btn_click = st.button("To konw more details about me Click here")

if btn_click == True:
    st.header("Thanks to veiw my profile")
    st.subheader("I am a B.Tech final year student. I am intrested in data science")
    st.header("My profile details are")
    bt_click = st.button("Linkedin")
    if btn_click == True:
        st.subheader("https://www.linkedin.com/in/eduru-teja-05391022a")

    bt_click = st.button("Github")
    if btn_click == True:
        st.subheader("https://github.com/tejaeduru123")
