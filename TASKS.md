# TASKS

CRUD build-out for the `inventory` app: **Houses, Professors, Students, Items**.
Broken into ~10 self-contained commits, each one leaving the app in a working state.

- [x] 1. Data model layer
  - Define `House`, `Professor`, `Student`, `Item` in `inventory/models.py`
    - `House`: name, founder, common_room, points
    - `Professor`: name, subject, office, house (FK → House, nullable, "head of house")
    - `Student`: name, year, house (FK → House), (FK → Professor, nullable)
    - `Item`: name, category, quantity, description, owner (FK → Student, nullable), house (FK → House, nullable)
  - `__str__` methods, register all four in `inventory/admin.py`
  - `makemigrations` + commit the migration file

- [x] 2. Houses — read views
  - `HouseListView`, `HouseDetailView` (or function-based equivalents)
  - `templates/inventory/house_list.html`, `house_detail.html`
  - URLs wired under `/houses/`

- [x] 3. Houses — write views
  - Create/Update/Delete views + `ModelForm`
  - `house_form.html`, `house_confirm_delete.html`
  - URLs: `/houses/new/`, `/houses/<pk>/edit/`, `/houses/<pk>/delete/`

- [ ] 4. Professors — read views
  - List + detail views/templates, URLs under `/professors/`

- [ ] 5. Professors — write views
  - Create/Update/Delete + form, templates, URLs

- [ ] 6. Students — read views
  - List + detail (show house and advisor), URLs under `/students/`

- [ ] 7. Students — write views
  - Create/Update/Delete + form (house/advisor as dropdowns), templates, URLs

- [ ] 8. Items — read views
  - List + detail (show owner/house), URLs under `/items/`

- [ ] 9. Items — write views
  - Create/Update/Delete + form, templates, URLs

- [ ] 10. Navigation & polish
  - Shared `base.html` with nav links to all four sections
  - Home page links into each list view
  - Light styling pass, README update (models, routes)

## Notes
- Each task should be its own commit with a message describing just that step (e.g. "Add Houses list and detail views").
- Run `python manage.py check` and click through the affected pages before committing each step.
- Migrations for later model tweaks (if any) get folded into the task that needs them, not bolted onto #10.
