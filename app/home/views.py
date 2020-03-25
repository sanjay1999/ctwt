from flask import abort, flash, redirect, render_template, url_for
from flask_login import login_required, current_user

from . import home
from .. import db
from ..models import Employee


@home.route('/')
def homepage():
    return render_template('home/index.html', title='Welcome to CTWT')


@home.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_admin == 1:
        return redirect(url_for('admin.admin_dashboard'))
    if current_user.is_lead == 1:
        lead = True
    else:
        lead = False
    return render_template('home/dashboard.html', title='Dashboard', lead=lead)


@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        abort(403)
    return render_template('home/admin_dashboard.html', title='Admin Dashboard')


@home.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():

    return render_template('home/profilepage.html', title='Employee Profile')
