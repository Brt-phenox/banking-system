# banking system

simple python banking system
cli interface with admin and user abilities
phase 2 simple bank management system

# 🏦 Simple CLI Banking Management System

A **Python-based terminal application** that simulates a banking environment with separate interfaces for **Users** and **Administrators**. The system uses a modular approach with **persistent JSON storage** to handle financial records securely.
easy to use and maintain

---

## ✨ Features

### 👤 User Features

- **Registration:** Create a new account with a starting balance of `0`.
- **Login System:** Authenticate using username and password.
- **Deposit:** Add funds to the account with real-time balance updates.
- **Check Balance:** Instantly view current available funds.
- **Transaction History:** Track and view a log of previous account activities.
- **Security:** Banned users are automatically blocked from logging in.

### 🛡️ Admin Features

- **Secure Access:** Protected by an admin-specific password (`admin123`).
- **User Oversight:** View a complete list of all registered users and their balances.
- **Account Control:** Ban users to restrict access to the system.

---

## 🛠️ Technical Overview

- **Language:** Python 3.x
- **Data Persistence:** JSON (`data.json`)
- **Architecture:** Modular design with a three-tier separation (main, user, admin)

---

## 📂 Project Structure

| File        | Description                                                         |
| ----------- | ------------------------------------------------------------------- |
| `main.py`   | Entry point. Handles file loading/saving and main portal selection. |
| `user.py`   | Contains user logic: registration, login, deposits, and history.    |
| `admin.py`  | Contains admin logic: viewing all users and banning accounts.       |
| `data.json` | Local database, created automatically on first run.                 |

---

## 💻 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/simple-cli-banking.git
cd simple-cli-banking
```
