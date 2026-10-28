from flask import Blueprint, render_template, request

from app.services.sentiment_service import analyze_review


analysis_bp = Blueprint("analysis", __name__, url_prefix="")


@analysis_bp.route("/single-analysis", methods=["GET", "POST"])
def single_analysis():
    result = None

    if request.method == "POST":
        review_text = request.form.get("review", "").strip()
        result = analyze_review(review_text)

    return render_template("single_analysis.html", title="Single Analysis", result=result)
