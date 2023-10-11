from flask import Blueprint, render_template

site1_bp = Blueprint('site1', __name__, url_prefix='/site1')

@site1_bp.route('/')
def hello():
  return render_template('site1/hello1.html')