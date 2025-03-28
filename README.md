# 🌐 Unit Converter API (Django)

A **Django REST framework (DRF) API** that allows users to convert between different measurement units, including **length, weight, and temperature**.

## 🚀 Features
✔ RESTful API for **unit conversions** (length, weight, temperature, etc.).  
✔ Uses **Django REST framework (DRF)** for easy API handling.  
✔ **Scalable and modular structure** following Django best practices.  
✔ **Supports JSON-based API requests and responses.**   

## 📌 Supported Conversions
### 📏 Length
- Millimeter (mm), Centimeter (cm), Meter (m), Kilometer (km)  
- Inch (in), Foot (ft), Yard (yd), Mile (mi)  

### ⚖ Weight
- Milligram (mg), Gram (g), Kilogram (kg)  
- Ounce (oz), Pound (lb)  

### 🌡 Temperature
- Celsius (°C), Fahrenheit (°F), Kelvin (K)  

---

## 🛠 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/UlashovaZahro/Unit_converter.git
cd Unit_converter
```

### 2️⃣ Create & Activate a Virtual Environment
```sh
python -m venv venv  # Create virtual environment
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 4️⃣ Apply Migrations & Run Server
```sh
python manage.py migrate
python manage.py runserver
```

---

## 🔥 API Endpoints
### Convert Length
```http
POST /api/convert/length/
```
#### Request Body (JSON)
```json
{
  "value": 100,
  "from_unit": "meter",
  "to_unit": "kilometer"
}
```
#### Response (JSON)
```json
{
  "from_unit": "meter",
  "to_unit": "kilometer",
  "value": 100,
  "convert_type": "Length",
  "result": 0.1
}
```

### Convert Weight
```http
POST /api/convert/weight/
```
#### Request Body (JSON)
```json
{
  "value": 200,
  "from_unit": "gram",
  "to_unit": "kilogram"
}
```
#### Response (JSON)
```json
{
  "from_unit": "gram",
  "to_unit": "kilogram",
  "value": 200,
  "convert_type": "Weight",
  "result": 0.2
}
```

### Convert Temperature
```http
POST /api/convert/temperature/
```
#### Request Body (JSON)
```json
{
  "value": 32,
  "from_unit": "fahrenheit",
  "to_unit": "celsius"
}
```
#### Response (JSON)
```json
{
  "from_unit": "fahrenheit",
  "to_unit": "celsius",
  "value": 32,
  "convert_type": "Temperature",
  "result": 0
}
```

## Project Roadmap

This project follows the guidelines provided by roadmap.sh. You can find the full project details here:
Unit Converter Roadmap - https://roadmap.sh/projects/unit-converter


