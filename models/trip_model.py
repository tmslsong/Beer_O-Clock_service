from my_app.models.user_model import find_user
from my_app import db

class Travel(db.Model):
    __tablename__= 'travel'

    id = db.Column(db.Integer, primary_key=True)
    trip_pref = db.Column(db.VARCHAR(200), nullable=False)
    user_name = db.Column(db.VARCHAR(200), db.ForeignKey('user.username'))

    def __repr__(self):
        return f"Beer Road Trip for {self.user_name}"


def update_trip_destination(inputname, destination):
    
    name_check = find_user(inputname).username

    trip_data = Travel(trip_pref=destination, user_name=name_check)

    db.session.add(trip_data)
    db.session.commit()