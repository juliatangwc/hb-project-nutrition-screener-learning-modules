"""Models for diet screener app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Screener(db.Model):
    """A record of screener results."""

    __tablename__ = 'screener'

    screener_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.String, db.ForeignKey("users.user_id"))
    completed_on = db.Column(db.DateTime)
    q1_veg_days = db.Column(db.Integer)
    q2_veg_qty = db.Column(db.Numeric(18,2))
    q3_fruit_days = db.Column(db.Integer)
    q4_fruit_qty = db.Column(db.Numeric(18,2))
    q5_rmeat_days = db.Column(db.Integer)
    q6_rmeat_qty = db.Column(db.Numeric(18,2))
    q7_pmeat_days = db.Column(db.Integer)
    q8_pmeat_qty = db.Column(db.Numeric(18,2))
    q9_wgrains_days = db.Column(db.Integer)
    q10_wgrains_qty = db.Column(db.Numeric(18,2))
    q11_rgrains_days = db.Column(db.Integer)
    q12_rgrains_qty = db.Column(db.Numeric(18,2))
    
    #Add relationship to user
    # progress = progress of this screener  < chage this to backpopulates

    def __repr__(self):
        return f'''<Screener screener_id={self.screener_id} user_id={self.user_id} 
                completed_on={self.completed_on}>'''


class Progress(db.Model):
    """A record to track screener completion progress."""

    __tablename__ = 'progress'

    progress_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    screener_id = db.Column(db.Integer, db.ForeignKey("screener.screener_id"))
    timestamp = db.Column(db.DateTime)
    screener_tracker = db.Column(db.Integer)

    screener = db.relationship("Screener", backref="progress")

    def __repr__(self):
        return f'''<Progress progress_id={self.progress_id} screener_id={self.screener_id}
                    screener_tracker={self.screener_tracker}>'''


def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)