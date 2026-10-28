# SentiScope

SentiScope is a Flask web app for analyzing the sentiment of customer reviews. Its single-review workflow preprocesses text and uses a trained scikit-learn model to return a positive, negative, or low-confidence neutral result.

## Features

- Analyze an individual review through the web interface.
- Clean review text with NLTK before vectorizing it with TF-IDF.
- Display the predicted sentiment and model confidence.
- Browse the landing page and preview planned bulk analysis, dashboard, and insights sections.

> Bulk CSV analysis, the dashboard, and business insights are currently placeholders and are not implemented workflows.

## Requirements

- Python 3.10 or later
- The NLTK `stopwords` and `wordnet` datasets

## Run locally

From the project root, create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux, activate it with:

```bash
source .venv/bin/activate
```

Install the Python dependencies and download the NLTK data used by preprocessing:

```bash
python -m pip install -r requirements.txt
python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet')"
```

Start the Flask development server:

```bash
python run.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. Submit a review from the Single Analysis page.

## Pages

| Path | Description |
| --- | --- |
| `/` | Home page |
| `/single-analysis` | Analyze one review |
| `/bulk-analysis` | Planned bulk-analysis page |
| `/dashboard` | Planned dashboard page |
| `/insights` | Planned insights page |
| `/about` | About SentiScope |

## Project structure

```text
app/
  blueprints/       Flask routes for the main pages and review analysis
  services/         Application-level sentiment analysis service
  static/           CSS, JavaScript, and images
  templates/        Jinja2 page templates
ml/
  datasets/         IMDB reviews dataset
  models/           Trained sentiment model and TF-IDF vectorizer
  preprocessing/    Shared text-cleaning functions
  predictor.py      Model inference
  01_sentiment_model_training.ipynb
config.py            Flask configuration
requirements.txt     Python dependencies
run.py               Application entry point
```

The trained model and vectorizer are loaded from `ml/models/` when the prediction module is imported; keep both files in place to run review analysis. The configured default database is SQLite (`app.db`), and the upload directory is `data/uploads/`.

## Configuration

The app reads `SECRET_KEY` and `DATABASE_URL` from environment variables. If they are not set, it uses a development secret and a local SQLite database. Set a secure `SECRET_KEY` before deploying the app; do not use the development default in production.

## Dependencies

See [`requirements.txt`](requirements.txt) for pinned versions, including Flask, Flask-SQLAlchemy, pandas, NumPy, scikit-learn, NLTK, and python-dotenv.
