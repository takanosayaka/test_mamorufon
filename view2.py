from flask import Blueprint, render_template

site2_bp = Blueprint('site2', __name__, url_prefix='/site2')

@site2_bp.route('/')
def hello():
  return render_template('site2/hello2.html')