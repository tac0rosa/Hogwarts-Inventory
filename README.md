# Hogwarts Inventory

A simple Django starter project for a small inventory-style website.

## Prerequisites

Make sure you have the following installed on your computer:

- Python 3.9+
- Git

## Clone the project

Open your terminal and run:

```bash
git clone <your-repo-url>
cd Hogwarts-Inventory
```

## Create and activate a virtual environment

On macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Run the project

Start the development server:

```bash
python manage.py runserver
```

Then open your browser and visit:

```text
http://127.0.0.1:8000/
```

## Useful commands

- Check if Django is configured correctly:

```bash
python manage.py check
```

- If you make changes to models, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Notes

If you see an error saying Django is not installed, make sure your virtual environment is activated before running the commands above.