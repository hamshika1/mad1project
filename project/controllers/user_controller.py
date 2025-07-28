from flask import Blueprint, render_template, session, redirect, url_for
from models.models import db, ParkingLot, ParkingSpot, Reservation

user_blueprint = Blueprint('user', __name__, url_prefix='/user')

@user_blueprint.route('/dashboard')
def dashboard():
    if not session.get('user_id'):
        return redirect(url_for('auth.login'))
    lots = ParkingLot.query.all()
    return render_template('user_dashboard.html', lots=lots)
