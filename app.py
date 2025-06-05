import streamlit as st
import analysis_and_model
import presentation

pages = {
    "Анализ и модель": analysis_and_model.main,
    "Презентация": presentation.main
}

st.sidebar.title("Навигация")
page = st.sidebar.radio("Выберите страницу:", list(pages.keys()))
pages[page]()