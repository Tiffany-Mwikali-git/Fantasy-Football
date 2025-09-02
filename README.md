

```
#  Fantasy Football (CLI-Based)

The **Football Application** is a proposed terminal-based application designed to help football lovers efficiently manage players, matches, and teams through a structured command-line interface. The system will be built using Python, leveraging SQLAlchemy ORM for database operations and Click for an enhanced CLI experience.

---

##  Purpose

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
- **SQLite** – Lightweight relational database
- **Virtual Environment** – `venv` or `pipenv` supported

---

##  Project Structure

```

fantasy football/
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

###  Clone the Repositoryfootball_fantasy

```bash
git clone https://github.com/tiffany-mwikali/fantasyfootball.git
cd fantasy football
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

##  ORM Overvie()`w

The database models will include:

* `Player`: One-to-many relationship with `Matches`
* `Player`: One-to-many relationship with `Teams`

Each model will implement:

* `create`
* `get_all`
* `find_by_id`

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


## License

MIT License

Copyright &copy; 2025 Tiffany Mwikali

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

