# RentEasy
A full-stack web application built using Django that allows users to list, browse, and manage rental properties.

---

## 🚀 Features

- 🔐 User Authentication (Login/Register)
- 🏡 Add & Manage Properties
- 📸 Property Image Uploads
- 🔍 Browse Available Rentals
- 🗂 Organized Django Apps (Accounts & Properties)

---

## 🛠 Tech Stack

- Backend: Django (Python)
- Database: SQLite
- Frontend: HTML, CSS (Django Templates)
- Media Handling: Django Media Files

---

## 📂 Project Structure


rental_project/
│── accounts/ # User authentication
│── properties/ # Property management
│── media/ # Uploaded images
│── db.sqlite3 # Database
│── manage.py


---

## ⚙️ Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/Rentify-Django.git
cd Rentify-Django
Create virtual environment:
python -m venv venv
venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Run migrations:
python manage.py migrate
Run server:
python manage.py runserver
