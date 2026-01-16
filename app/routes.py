from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def home (): 
    return render_template('home.html', title='Home Page')

@bp.route('/manual')
def manual(): 
    return render_template('manual.html', title='Manual Control')

@bp.route('/auto/setup')
def auto_setup(): 
    return render_template('auto_setup.html', title='Auto Setup')

@bp.route('/auto/montor')
def auto_monitor(): 
    return render_template('auto_monitor.html', title='Auto Monitor')