from flask_security import SQLAlchemyUserDatastore, Security

from app import db, app
from models import User, Role


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
