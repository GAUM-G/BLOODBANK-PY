# 🩸 Blood Bank Management System

## 📌 Overview
The **Blood Bank Management System** is a GUI-based Python application that helps manage blood donations and requests using a MySQL database. It allows users to donate or request blood and updates the database accordingly.

## 🚀 Features
- 🏥 **Blood Donation Management**
- 💉 **Blood Request Handling**
- 🔍 **View Available Blood Units**
- 🔄 **Real-time Database Updates**
- 🛡 **Error Handling & Secure Database Operations**

## 🛠 Technologies Used
- **Python** (for the main application logic)
- **Tkinter** (for GUI)
- **MySQL** (for database management)
- **MySQL Connector for Python**

## 📂 Database Setup
1. **Create Database**
```sql
CREATE DATABASE db;
USE db;
```
2. **Create BloodBank Table**
```sql
CREATE TABLE BloodBank (
    Blood_Grp VARCHAR(10) PRIMARY KEY,
    units INT
);
```
3. **Insert Sample Data**
```sql
INSERT INTO BloodBank (Blood_Grp, units) VALUES ('A+', 10), ('B+', 12), ('O+', 15), ('AB+', 8);
```

## 📥 Installation
### 1️⃣ Install MySQL Connector
```sh
pip install mysql-connector-python
```
### 2️⃣ Run the Python Script
```sh
python bloodbank.py
```

## 📖 How to Use
1. Run the script, and the GUI will open.
2. View available blood groups and their units.
3. Click **Donate** to add blood units.
4. Click **Request** to request blood.
5. Receive success or error messages based on availability.
6. Exit when done.

## 🛡 Security & Improvements
- ✅ **Parameterized Queries** to prevent SQL injection.
- ✅ **Error Handling** to prevent crashes.
- ✅ **Optimized GUI for User Experience.**

## 📜 License
This project is free to use and modify. 😊
