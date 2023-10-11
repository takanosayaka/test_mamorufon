from flask import Blueprint, render_template

intercom_bp = Blueprint('intercom', __name__, url_prefix='/intercom')

@intercom_bp.route('/')
def display():
  return render_template('intercom/home.html')