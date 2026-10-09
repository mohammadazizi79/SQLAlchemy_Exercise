
# 🐍 SQLAlchemy Exercises

A collection of Python projects focused on learning **SQLAlchemy ORM**, database management, and relationships between database tables using SQLite.

---

## 📚 Projects

### 🛒 1. DigiShop — Product & User Management

A simple database application designed to practice SQLAlchemy ORM and essential database operations.

**Features**
- 🗃️ Creating database tables and defining ORM models
- ➕ Adding users and products
- 🔍 Querying and filtering database records
- ✏️ Updating existing records
- 🗑️ Deleting records

**Database Models**

| Model | Description |
|---|---|
| `User` | Stores user information, including name, address, and score |
| `Product` | Stores product information, including name, quantity, price, and rating |

**Main File:** `main.py`

### 🌐 2. Social Media — Users & Posts

A database project demonstrating how users and their posts can be connected through SQLAlchemy relationships.

**Features**
- 🧱 Defining ORM models
- 🔗 Creating foreign key relationships
- 🔄 Implementing one-to-many relationships
- 🧩 Using `relationship()` and `back_populates`
- 👤 Accessing a user's posts through ORM relationships
- 🔎 Querying related objects

**Database Models**

| Model | Description |
|---|---|
| `User` | Stores user information and provides access to associated posts |
| `Post` | Stores post information and references its owner |

**Main File:** `relationship.py`

---

## 🛠️ Technologies

- **Python** — Programming language
- **SQLAlchemy ORM** — Object-relational mapping and database operations
- **SQLite** — Lightweight relational database
- **Git & GitHub** — Version control and project hosting

---

## 📁 Project Structure

```text
SQLAlchemy_Exercise/
├── main.py
├── relationship.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the Repository

Replace the placeholder with your GitHub repository URL.

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Navigate to the Project Directory

```bash
cd SQLAlchemy_Exercise
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Running the Projects

Run the DigiShop project:

```bash
python main.py
```

Run the Social Media project:

```bash
python relationship.py
```

The scripts initialize their SQLite database tables automatically. Database files are created locally when needed.

---

## 🎯 Learning Objectives

These projects provide hands-on practice with:

- SQLAlchemy ORM fundamentals
- Defining models and creating database tables
- CRUD operations: Create, Read, Update, and Delete
- Querying and filtering database records
- Primary keys and foreign keys
- One-to-many relationships
- Navigating relationships between ORM objects
- Managing SQLite databases with Python

---

## 📝 Notes

- These projects are educational exercises for practicing SQLAlchemy ORM.
- SQLite database files are excluded from version control using `.gitignore`.
- Running the scripts may create or modify local database records.
- Review deletion operations before running the DigiShop script to avoid unintentionally removing records.

---

## 👨‍💻 Author

**Mohammad Azizi**

---

⭐ *Built to practice Python, SQLAlchemy ORM, and relational database concepts.*