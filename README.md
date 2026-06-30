# Cyber Portfolio Tracker

A web app for cybersecurity students to log certifications, CTF wins, labs, and projects, and share a clean public portfolio link with recruiters.

## Features (MVP)

- Account registration & login (hashed passwords, session-based auth via Flask-Login)
- Add / delete portfolio entries across 5 categories: Certification, CTF, Project, Lab, Skill
- Private dashboard with per-category counts and client-side filtering
- Public, shareable, read-only portfolio page at `/u/<username>`
- JSON API (`/api/entries`) for your own entries (authenticated)

## Tech Stack

- **Backend:** Python 3.10+, Flask, Flask-SQLAlchemy, Flask-Login
- **Database:** SQLite (file-based, zero config — swap via `DATABASE_URL` env var later)
- **Frontend:** Jinja2 templates, vanilla CSS, vanilla JavaScript (no build step)

## Project Structure

```
cyber-portfolio-tracker/
├── app/
│   ├── __init__.py          # App factory
│   ├── extensions.py        # db, login_manager instances
│   ├── models.py            # User, PortfolioEntry
│   ├── routes/
│   │   ├── auth.py          # register/login/logout
│   │   ├── portfolio.py     # dashboard, CRUD, public view
│   │   └── api.py           # JSON endpoint
│   ├── templates/
│   └── static/
│       ├── css/style.css
│       └── js/main.js
├── tests/
│   └── test_basic.py
├── config.py
├── run.py
├── requirements.txt
└── .gitignore
```

## Setup

1. **Clone and enter the project**
   ```bash
   git clone <your-repo-url>
   cd cyber-portfolio-tracker
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables** (recommended — create a `.env` file)
   ```
   SECRET_KEY=replace-with-a-random-secret
   FLASK_ENV=development
   ```

5. **Run the app**
   ```bash
   python run.py
   ```
   The database is created automatically on first run at `instance/app.db`. Visit `http://127.0.0.1:5000`.

## Running Tests

```bash
python -m pytest tests/ -v
```

## Security Notes for Contributors

- All entry mutation routes verify `entry.user_id == current_user.id` before allowing edits/deletes.
- Links are restricted to `http://`/`https://` schemes to prevent `javascript:` URI injection.
- Passwords are hashed with Werkzeug's `generate_password_hash` (PBKDF2) — never stored in plaintext.
- `SECRET_KEY` **must** be overridden via environment variable in any non-local deployment.
- CSRF protection is not yet implemented — see open issues. Don't deploy publicly until that's addressed.

## Roadmap (post-MVP)

- CSRF protection (Flask-WTF)
- Edit existing entries (currently add/delete only)
- Login rate limiting
- File/screenshot uploads for proof of work
- Tagging and search across entries
- PDF export of public portfolio
