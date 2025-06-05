import streamlit as st
import reveal_slides as rs

def main():
    st.title("Презентация проекта")
    presentation_markdown = """
    ## Прогнозирование отказов оборудования
    ---
    **Цели проекта:**
    - Разработка модели бинарной классификации
    - Создание интерактивного приложения
    - Визуализация результатов
    
    **Технологии:**
    - Python (Pandas, Scikit-learn)
    - Streamlit
    - Random Forest
    
    **Результаты:**
    - Точность модели: 96%
    - Автоматизированное предсказание отказов
    
    **Инструкция по использованию:**
    1. На странице "Анализ и модель" загрузите CSV-файл с данными
    2. Система автоматически обучит модель
    3. Используйте форму для прогнозирования состояния оборудования
    """
    st.markdown(presentation_markdown)
    
    st.image("https://miro.medium.com/v2/resize:fit:720/format:webp/1*QZAB_v1mN6HVD8l-7p0m3g.png", 
             caption="Пример предиктивного обслуживания")
    with st.sidebar:
        st.header("Настройки презентации")
        theme = st.selectbox("Тема", ["black", "white", "league", "beige",
        "sky", "night", "serif", "simple", "solarized"])
        height = st.number_input("Высота слайдов", value=500)
        transition = st.selectbox("Переход", ["slide", "convex", "concave",
        "zoom", "none"])
        plugins = st.multiselect("Плагины", ["highlight", "katex",
        "mathjax2", "mathjax3", "notes", "search", "zoom"], [])
        # Отображение презентации
    rs.slides(
    presentation_markdown,
    height=height,
    theme=theme,
    config={
    "transition": transition,
    "plugins": plugins,
    },
    markdown_props={"data-separator-vertical": "^--$"},
    )