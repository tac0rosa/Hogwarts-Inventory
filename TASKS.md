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

- [x] 4. Professors — read views
  - List + detail views/templates, URLs under `/professors/`

- [x] 5. Professors — write views
  - Create/Update/Delete + form, templates, URLs

- [x] 6. Students — read views
  - List + detail (show house and advisor), URLs under `/students/`

- [x] 7. Students — write views
  - Create/Update/Delete + form (house/advisor as dropdowns), templates, URLs

- [ ] 8. Items — read views
  - List + detail (show owner/house), URLs under `/items/`

- [ ] 9. Items — write views
  - Create/Update/Delete + form, templates, URLs

- [ ] 10. Navigation & polish
  - Shared `base.html` with nav links to all four sections
  - Home page links into each list view
  - Light styling pass, README update (models, routes)

## Documentation
Lives in `DOKUMENTATION.md` (written in German). Filled in gradually, alongside the rest of the tasks — not all at once at the end.

- [ ] D1. Motivation and requirements — project idea, team, problem statement, existing solutions (doesn't depend on the code, can be done now)
- [ ] D2. Planning and design — task distribution, framework/environment/tools, DB diagram (do after #1; revisit if the model changes)
- [ ] D3. Development — features (screenshots) and technical challenges (code snippets); add one block per finished CRUD section: Houses (after #2-3), Professors (after #4-5), Students (after #6-7), Items (after #8-9)
- [ ] D4. Getting started — steps to run the project locally (can lean on the README; do near #10)
- [ ] D5. Conclusion — which initial requirements were implemented, personal assessment, possible future improvements (at the end, after #10)
- [ ] D6. Sources — links to libraries/docs and any third-party code used (note these as they come up, don't leave it for the end)
It has to be around 15 pages and it can contain screenshots.

## Notes
- Each task should be its own commit with a message describing just that step (e.g. "Add Houses list and detail views").
- Run `python manage.py check` and click through the affected pages before committing each step.
- Migrations for later model tweaks (if any) get folded into the task that needs them, not bolted onto #10.
