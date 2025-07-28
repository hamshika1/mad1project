from flask import Flask
from models.models import db, create_admin
from controllers.auth_controller import auth_blueprint
from controllers.admin_controller import admin_blueprint
from controllers.user_controller import user_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = 'your_secret_key'

# Initialize DB
db.init_app(app)

with app.app_context():
    db.create_all()
    create_admin()  # Create default admin if not exists

# Register Blueprints
app.register_blueprint(auth_blueprint)
app.register_blueprint(admin_blueprint)
app.register_blueprint(user_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

