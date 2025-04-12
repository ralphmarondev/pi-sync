# 🧠 PiSync API

Welcome to the **PiSync API**, the **brain of the system**.  
This backend is the **single source of truth** — it stores and manages all critical data shared across the Android, Desktop, Web, and Raspberry Pi components of the project.

---

## 🚀 Getting Started

Follow these steps to set up and run the API locally.

---

### 📁 Project Structure

When you download the repository, this API is located under:

```
pi-sync/
│
├── api/              ← You are here (backend)
├── android/          ← Android app
├── desktop/          ← Desktop client
├── web/              ← Web client
├── raspberrypi/      ← Raspberry Pi scripts
├── README.md         ← Root documentation
└── LICENSE
```

---

### 1. Navigate to the API folder

```bash
cd pi-sync/api
```

---

### 2. Create and activate a virtual environment

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Set up the PostgreSQL database

Ensure PostgreSQL is installed and running.

Create a database with the following details:

- **Database name:** `pisync`
- **Username:** `postgres`
- **Password:** `postgres`
- **Host:** `localhost`
- **Port:** `5432`

---

### 5. Run migrations

First, make sure your database schema is up-to-date by running:

```bash
python manage.py makemigrations
```

Then apply the migrations:

```bash
python manage.py migrate
```

---

### 6. Start the development server

```bash
python manage.py runserver
```

Your API will now be accessible at `http://localhost:8000/`.

---

## ✅ Notes

- Make sure your PostgreSQL credentials match what’s in your `settings.py` or environment config.
- You can use tools like [Postman](https://www.postman.com/) or [Hoppscotch](https://github.com/hoppscotch/hoppscotch/) to test your endpoints.

---

## 🧑‍💻 Author

Built with care by [Ralph Maron Eda](https://github.com/ralphmarondev)
