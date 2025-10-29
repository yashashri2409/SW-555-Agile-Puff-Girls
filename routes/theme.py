from flask import Blueprint, jsonify, request, render_template
from extensions import db
from models import ThemePreference

theme_bp = Blueprint("theme", __name__, url_prefix="/theme")


@theme_bp.route("/settings")
def theme_settings():
    """Get current theme settings."""
    # Get current user's theme preference (you might need to adjust this based on your auth system)
    theme = ThemePreference.query.first()
    return jsonify({"theme": theme.preference if theme else "light"})


@theme_bp.route("/toggle", methods=["POST"])
def toggle_theme():
    """Toggle theme preference."""
    data = request.get_json()
    theme = data.get("theme")

    if theme not in ["light", "dark"]:
        return jsonify({"error": "Invalid theme value"}), 400

    # Update or create theme preference (adjust based on your auth system)
    preference = ThemePreference.query.first()
    if preference:
        preference.preference = theme
    else:
        preference = ThemePreference(preference=theme)
        db.session.add(preference)

    db.session.commit()

    return jsonify({"success": True, "theme": theme})
