from flask import Blueprint, render_template, redirect, url_for, session
from models.models import db, ParkingLot, ParkingSpot

admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@admin_blueprint.route('/dashboard')
def dashboard():
    if not session.get('admin'):
        return redirect(url_for('auth.login'))
    lots = ParkingLot.query.all()
    return render_template('admin_dashboard.html', lots=lots)
