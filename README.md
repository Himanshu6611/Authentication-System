🔐 Authentication-System

This project implements a traditional authentication system using Flask and MySQL. It allows users to register, log in, and securely authenticate using a username and password. The system validates user credentials from the database and redirects authenticated users to a personalized dashboard.

📖 Overview

This application demonstrates a basic yet secure traditional authentication method using a username and password. It features a clean UI, real-time validation, session handling, and database verification—perfect for college projects, demos, or learning full-stack development.

✨ Features

🔹 User Registration

Collects Name, Username, Email, and Password

Prevents duplicate usernames

Stores data in MySQL

🔹 Two-Step Login

Enter Username → System checks if it exists

Enter Password → Validated with database

🔹 Dashboard

Displays a personalized message:

Welcome, <User Name>!

🔹 Error Handling

Invalid username

Wrong password

Duplicate account on signup

🧰 Tech Stack
Component	Technology

Frontend	HTML, CSS, JavaScript

Backend	Python Flask

Database	MySQL

Styling	Custom CSS

Logic	Form validation + SQL queries

📂 Project Structure

p1/



├── static/

│   ├── style.css

│   └── script.js

│
├── templates/

│   ├── signup.html

│   ├── login.html

│   ├── enter_password.html

│   └── dashboard.html

│
└── app.py


🗄️ Database Schema
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    username VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

⚙️ Installation & Setup

✔ 1. Clone the Repository
git clone <your-repo-url>
cd p1

✔ 2. Install Dependencies
pip install flask mysql-connector-python

✔ 3. Create MySQL Database
CREATE DATABASE biometric_lab;
USE biometric_lab;

✔ 4. Run the Application
python app.py

✔ 5. Open in Browser
http://127.0.0.1:5000


▶️ Usage

Register a new user through the signup page.

Go to the login page.

Enter username → proceed.

Enter password → authenticate.

Successful login redirects to the dashboard.

🏁 Conclusion

This project demonstrates a complete traditional authentication system built using Flask and MySQL. It is ideal for academic submissions, learning backend development, or demonstrating secure login authentication.
