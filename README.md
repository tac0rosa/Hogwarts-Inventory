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

## Data model

Four models live in `inventory/models.py`, all registered in the Django admin (`/admin/`) as well as their own CRUD views:

- **House** — `name` (unique), `founder`, `common_room`, `points`
- **Professor** — `name`, `subject`, `office`; `house` (optional — the house they're head of)
- **Student** — `name`, `year`; `house` (required); `advisor` (optional, a `Professor`)
- **Item** — `name`, `category`, `quantity`, `description`; `house` (required); `owner` (optional, a `Student`)

Deleting a `House` cascades to its `Student`s and `Item`s. Deleting a `Professor` or a `Student` only clears the optional `advisor`/`owner` references pointing to them — nothing else is deleted.

## Routes

Each of the four sections (Houses, Professors, Students, Items) exposes the same five routes:

| Path | Purpose |
| --- | --- |
| `/<section>/` | List view |
| `/<section>/new/` | Create form |
| `/<section>/<pk>/` | Detail view |
| `/<section>/<pk>/edit/` | Edit form |
| `/<section>/<pk>/delete/` | Delete confirmation |

For example, Houses: `/houses/`, `/houses/new/`, `/houses/<pk>/`, `/houses/<pk>/edit/`, `/houses/<pk>/delete/`. The same pattern applies under `/professors/`, `/students/`, and `/items/`. The home page (`/`) links into all four list views.

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