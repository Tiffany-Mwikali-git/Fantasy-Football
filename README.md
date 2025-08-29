

```
#  Fantasy Football (CLI-Based)

The **Football Application** is a proposed terminal-based application designed to help football lovers efficiently manage players, matches, and teams through a structured command-line interface. The system will be built using Python, leveraging SQLAlchemy ORM for database operations and Rich for an enhanced CLI experience.

---

## 📌 Purpose

This system aims to digitize and simplify football operations by offering a reliable and interactive way to manage football.

---

##  Key Features

###  Manage Players
- Add name of the player.
- Position of the player.
- Goals of the player.

###  Manage Matches
- List of matches.
- Add match.
- Date of when they will be played
- Predict the final score

###  Manage Teams
- List the teams.
- Add teams.
- list weather team will play away or home.

---

##  Technology Stack

- **Python 3.12.3**
- **SQLAlchemy** – ORM for database management
- **Rich** – Library for beautiful CLI rendering
- **SQLite** – Lightweight relational database
- **Virtual Environment** – `venv` or `pipenv` supported

---

##  Project Structure

```

gym\_cli/
├── app/
│   ├── cli.py              # Main program entry point
│   ├── actions.py          # Logic handlers
│   ├── menus.py            # CLI menu structure
│   ├── __init_.py           
│   ├── models/
│   │   ├── base.py         # Database session setup
│   │   ├── match.py       # match model
│   │   ├── players.py      # players model
│   │   └── teams.py     # teams model
├── Pipfile / requirements.txt
└── README.md

````

---

## Setup Instructions

###  Clone the Repository

```bash
git clone https://github.com/tiffany-mwikali/fantasyfootball_cli.git
cd fantasy football_cli
````

### 2️ Create a Virtual Environment

#### Option A: Using `venv`

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

#### Option B: Using `pipenv`

```bash
pipenv install
pipenv shell
```

###  Run the Application

```bash
python -m app.cli
```

---

##  ORM Overview

The database models will include:

* `Player`: One-to-many relationship with `Matches`
* `Player`: One-to-many relationship with `Teams`

Each model will implement:

* `create()`
* `get_all()`
* `find_by_id()`

---

##  Example CLI Menu

```
FANTASY FOOTBALL MANAGER

[1] Manage Matches
[2] Manage Teams
[3] Manage Players
[5] Exit

Choose:
```

---

## Development Tools

To reset the system (dev use only), a utility will be provided to delete all database rows.

---

## License

This project will be released under the **MIT License**.

---

