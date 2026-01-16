from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home (): 
    return render_template('index.html', title='Home Page')

@main.route('/manual')
def manual(): 
    return render_template('manual.html', title='Manual Control')

@main.route('/auto/setup')
def auto_setup(): 
    return render_template('auto_setup.html', title='Auto Setup')

@main.route('/auto/monitor')
def auto_monitor(): 
    return render_template('auto_monitor.html', title='Auto Monitor')