import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from ucimlrepo import fetch_ucirepo

def main():
    st.title("Анализ данных и модель")
    
    # Загрузка данных
    data = load_data()
    if data is None:
        return
    
    # Предобработка
    data = preprocess_data(data)
    
    # Разделение данных
    X_train, X_test, y_train, y_test = split_data(data)
    
    # Обучение модели
    model = train_model(X_train, y_train)
    
    # Оценка
    evaluate_model(model, X_test, y_test)
    
    # Предсказания
    prediction_form(model)

def load_data():
    if st.checkbox("Использовать встроенные данные"):
        dataset = fetch_ucirepo(id=601)
        return pd.concat([dataset.data.features, dataset.data.targets], axis=1)
    else:
        uploaded_file = st.file_uploader("Загрузите CSV", type="csv")
        return pd.read_csv(uploaded_file) if uploaded_file else None

def preprocess_data(data):
    data = data.drop(columns=['UDI', 'Product ID', 'TWF', 'HDF', 'PWF', 'OSF', 'RNF'])
    data['Type'] = LabelEncoder().fit_transform(data['Type'])
    scaler = StandardScaler()
    num_cols = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
    data[num_cols] = scaler.fit_transform(data[num_cols])
    return data

def split_data(data):
    X = data.drop(columns=['Machine failure'])
    y = data['Machine failure']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    st.subheader("Оценка модели")
    st.metric("Accuracy", f"{accuracy_score(y_test, y_pred):.2%}")
    
    fig, ax = plt.subplots()
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', ax=ax)
    st.pyplot(fig)
    
    st.text(classification_report(y_test, y_pred))

def prediction_form(model):
    with st.form("prediction_form"):
        st.write("**Параметры оборудования:**")
        col1, col2 = st.columns(2)
        air_temp = col1.number_input("Температура воздуха (K)", value=300.0)
        process_temp = col2.number_input("Температура процесса (K)", value=310.0)
        rotational_speed = col1.number_input("Скорость вращения (rpm)", value=1500)
        torque = col2.number_input("Крутящий момент (Nm)", value=40.0)
        tool_wear = col1.number_input("Износ инструмента (min)", value=100)
        type_val = col2.selectbox("Тип оборудования", ["L", "M", "H"])
        
        if st.form_submit_button("Предсказать"):
            input_data = pd.DataFrame({
                'Type': [{"L":0, "M":1, "H":2}[type_val]],
                'Air temperature [K]': [air_temp],
                'Process temperature [K]': [process_temp],
                'Rotational speed [rpm]': [rotational_speed],
                'Torque [Nm]': [torque],
                'Tool wear [min]': [tool_wear]
            })
            prediction = model.predict(input_data)[0]
            proba = model.predict_proba(input_data)[0][1]
            st.success(f"Прогноз: {'Отказ' if prediction == 1 else 'Норма'} (Вероятность отказа: {proba:.1%})")