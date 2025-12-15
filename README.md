


# 📚 Library Management System API

A RESTful **Library Management System API** designed as a capstone project. This API allows you to manage users, books, and book checkout/return workflows with proper data modelling, validation, and authentication.

---

## 🚀 Features

* User management (create, list, retrieve, update)
* Book management (CRUD operations)
* Checkout and return books
* Track currently borrowed and available books
* Enforces availability rules
* Token-based authentication (JWT or DRF Token)
* Clean relational data model (ERD-driven design)

---

## 🧱 System Design

### Entity Relationship Diagram (ERD)

The system is built around three core entities:

#### **User**

| Field | Type      | Notes                |
| ----- | --------- | -------------------- |
| id    | PK (auto) | Primary key          |
| name  | string    | User's full name     |
| email | string    | Unique email address |

#### **Book**

| Field        | Type    | Notes                       |
| ------------ | ------- | --------------------------- |
| id           | PK      | Primary key                 |
| title        | string  | Book title                  |
| author       | string  | Book author                 |
| isbn         | string  | Unique ISBN                 |
| is_available | boolean | Current availability status |

#### **Checkout**

| Field         | Type                | Notes                         |
| ------------- | ------------------- | ----------------------------- |
| id            | PK (auto)           | Primary key                   |
| user_id       | FK → User.id        | Borrowing user                |
| book_id       | FK → Book.id        | Borrowed book                 |
| checkout_date | datetime            | When the book was checked out |
| return_date   | datetime (nullable) | When the book was returned    |

---

### 🔗 Relationships

* **User 1 → M Checkout**
  A user can have many checkout transactions.

* **Book 1 → M Checkout**
  A book can be checked out many times over its lifetime, but only once at a time.

---

## 🔒 Constraints & Indexes

* Primary keys on all tables
* Foreign key constraints on `Checkout.user_id` and `Checkout.book_id`
* Unique constraints:

  * `User.email`
  * `Book.isbn`
* Index recommended on `Checkout.return_date` to efficiently query borrowed books currently

---

## 🔐 Authentication

* Token-based authentication using **JWT** or **Django Rest Framework Tokens**
* Checkout and return endpoints are protected

---

## ✅ Business Rules & Validation

* A book **must be available** (`is_available = true`) to be checked out
* When a book is checked out:

  * `is_available` is set to `false`
* When a book is returned:

  * `return_date` is set
  * `is_available` is set to `true`
* (Optional) Enforce single-copy checkout per user via business logic

---

## 📡 API Endpoints

### 👤 Users

| Method | Endpoint       | Description                      |
| ------ | -------------- | -------------------------------- |
| POST   | `/users/`      | Create a new user                |
| GET    | `/users/`      | List users (pagination optional) |
| GET    | `/users/{id}/` | Retrieve user details            |
| PUT    | `/users/{id}/` | Update user details              |

**Create / Update User Body**

```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

---

### 📖 Books

| Method | Endpoint       | Description                    |
| ------ | -------------- | ------------------------------ |
| POST   | `/books/`      | Add a new book                 |
| GET    | `/books/`      | List books (filters supported) |
| GET    | `/books/{id}/` | Retrieve book details          |
| PUT    | `/books/{id}/` | Update book                    |
| DELETE | `/books/{id}/` | Delete book                    |

**Add / Update Book Body**

```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "isbn": "9780132350884"
}
```

**Supported Filters**

* `author`
* `title`
* `available` (true/false)

---

### 🔄 Checkout & Return

| Method | Endpoint      | Description                   |
| ------ | ------------- | ----------------------------- |
| POST   | `/checkout/`  | Checkout a book               |
| POST   | `/return/`    | Return a book                 |
| GET    | `/borrowed/`  | List currently borrowed books |
| GET    | `/available/` | List available books          |

**Checkout / Return Body**

```json
{
  "user_id": 1,
  "book_id": 5
}
```

---

## 🛠️ Tech Stack (Suggested)

* **Backend:** Django + Django REST Framework
* **Database:** PostgreSQL / SQLite
* **Auth:** JWT or DRF Token Authentication
* **ORM:** Django ORM

---

## 📦 Installation (Example)

```bash
git clone https://github.com/yourusername/library-management-api.git
cd library-management-api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🧪 Testing

* Unit tests recommended for:

  * Book availability logic
  * Checkout/return flows
  * Auth-protected endpoints

---

## 📈 Future Enhancements

* Due dates & overdue tracking
* Fines & notifications
* Admin dashboard
* Soft deletes
* Rate limiting

---

## 📝 License

This project is created for educational purposes as part of a capstone assignment.

---

## 🙌 Author

Capstone Project – Library Management System API
