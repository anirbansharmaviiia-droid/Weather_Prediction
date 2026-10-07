# 🌦️ Weather Prediction Web App

A simple and responsive weather application built with **Django** and the **OpenWeather API**.

Users can enter the name of a city and get real-time weather information including temperature, feels-like temperature, humidity, pressure, weather description, wind speed, and weather icons.

---

## 🚀 Features

- 🌍 Search weather by city name
- 🌡️ Current temperature in Celsius
- 🤒 Feels-like temperature
- 💧 Humidity information
- 📊 Atmospheric pressure
- 🌤️ Weather condition and description
- 💨 Wind speed
- 🖼️ Dynamic weather icons
- ❌ Error handling for invalid cities
- 🔐 API key stored securely using environment variables
- 🐍 Built with Django and Python

---

## 🛠️ Technologies Used

- **Python**
- **Django**
- **HTML**
- **CSS**
- **OpenWeather API**
- **Requests**
- **python-dotenv**
- **SQLite**

---

## 📁 Project Structure

```text
weather_prediction/
│
├── authentication/
│   ├── migrations/
│   ├── templates/
│   │   └── authentication/
│   │       └── home.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── weather_prediction/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── venv/
├── .env
├── .gitignore
├── db.sqlite3
├── manage.py
└── README.md
