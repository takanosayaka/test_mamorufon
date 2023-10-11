from flask import Blueprint, render_template

monitor_bp = Blueprint('monitor', __name__, url_prefix='/monitor')

@monitor_bp.route('/')
def display():
  return render_template('monitor/home2.html')