"""Generic status/version route — boilerplate, unrelated to the rest of this PR."""

from flask import Blueprint, jsonify

status_bp = Blueprint("status", __name__)


@status_bp.route("/status")
def status():
    return jsonify({"version": "0.1.0", "uptime": "n/a"})
