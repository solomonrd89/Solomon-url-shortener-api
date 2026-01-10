# 🚀 Scalable URL Shortener API

A high-performance RESTful API built with **Python (Flask)** and **MySQL** designed to handle URL redirection and click tracking. 

This project demonstrates **System Design** principles including **MVC Architecture**, **Optimistic Concurrency Control**, and **Database Efficiency**.

## 🛠️ Key Features (System Design)
* **Robust Architecture:** Follows the **Model-View-Controller (MVC)** pattern for separation of concerns and scalability.
* **Concurrency Handling:** Implements **Optimistic Locking** (Try/Catch retry logic) to handle hash collisions and race conditions without locking the database.
* **Efficient Database Access:** Uses **PyMySQL** with connection management to handle multiple requests efficiently.
* **Security:** Environment variables (`.env`) used for sensitive credentials; SQL injection prevention via parameterized queries.

## ⚙️ Tech Stack
* **Backend:** Python 3.10+, Flask
* **Database:** MySQL (Relational DB for ACID compliance)
* **Driver:** PyMySQL (Pure Python MySQL Client)
* **Tools:** Postman (API Testing), Git/GitHub

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone [https://github.com/solomonrd89/Solomon-url-shortener-api.git](https://github.com/solomonrd89/Solomon-url-shortener-api.git)
   cd Solomon-url-shortener-api