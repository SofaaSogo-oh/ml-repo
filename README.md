# Проект: Бинарная классификация для предиктивного обслуживания оборудования
## Цель проекта
Разработать модель машинного обучения, которая предсказывает, произойдет ли отказ оборудования (Target = 1) или нет (Target = 0). Результаты оформлены в виде интерактивного Streamlit-приложения.

## Описание датасета
- **Источник:** [UCI AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/dataset/601/predictive+maintenance+dataset)
- **Объем:** 10,000 записей
- **Признаки:** температура, крутящий момент, скорость вращения, износ и др.
- **Целевая переменная:** `Machine failure` (0 или 1)

## Модель
- **Алгоритм:** Random Forest
- **Метрики оценки:**
  - Accuracy
  - ROC-AUC
  - Confusion Matrix
- **Предобработка:**
  - Удалены лишние признаки (UDI, Product ID, TWF и др.)
  - Кодирование `Type`
  - Масштабирование признаков

## Возможности приложения
Приложение позволяет:
- Загружать данные (CSV)
- Обучать модель и визуализировать метрики
- Вводить новые значения и получать предсказание

## Установка
```bash
git clone https://github.com/SofaaSogo-oh/ml-repo.git  predictive_maintenance_project
cd predictive_maintenance_project
pip install -r requirements.txt
streamlit run app.py
```

[Видео-демонстрация работы приложения (относительная)](video/ml-demo.mp4)

[Видео-демонстрация работы приложения (ссылка для скачивания)](https://github.com/SofaaSogo-oh/ml-repo/raw/main/video/ml-demo.mp4)
