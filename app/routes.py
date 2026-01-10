from flask import Blueprint, request, jsonify, redirect
from .services import create_short_url, get_original_and_track

# Create a Blueprint (a modular group of routes)
main = Blueprint("main", __name__)


@main.route("/")
def home():
    return jsonify({"message": "Pro URL Shortener API is Running", "status": "active"})


@main.route("/shorten", methods=["POST"])
def shorten():
    data = request.get_json()

    # Basic Validation
    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    # Logic Handoff
    try:
        short_code = create_short_url(data["url"])
        return (
            jsonify(
                {
                    "short_url": f"http://127.0.0.1:5000/{short_code}",
                    "short_code": short_code,
                }
            ),
            201,
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@main.route("/<short_code>")
def redirect_url(short_code):
    original_url = get_original_and_track(short_code)

    if original_url:
        return redirect(original_url)

    return jsonify({"error": "URL not found"}), 404
