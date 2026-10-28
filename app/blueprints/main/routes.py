from flask import Blueprint, render_template


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def index():
    return render_template("index.html", title="SentiScope")


@main_bp.route("/bulk-analysis")
def bulk_analysis():
    return render_template("bulk_analysis.html", title="Bulk Analysis")


@main_bp.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", title="Dashboard")


@main_bp.route("/insights")
def insights():
    return render_template("insights.html", title="Insights")


@main_bp.route("/about")
def about():
    return render_template("about.html", title="About")
