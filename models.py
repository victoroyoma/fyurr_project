import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Venue(db.Model):
    __tablename__ = 'venues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(100)), default=[])
    image_link = db.Column(db.String(500))
    website_link = db.Column(db.String(120), default=None)
    facebook_link = db.Column(db.String(120))
    looking_for_talent = db.Column(db.Boolean(), default=False)
    seeking_description = db.Column(db.String(200), default=None)
    date_created = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
    shows = db.relationship('Show', backref='venue', lazy=True)
    
    def __str__(self):
        return f'Name:{self.name}'

    # TODO: implement any missing fields, as a database migration using Flask-Migrate


class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String(100)), default=[])
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120))
    looking_for_venues = db.Column(db.Boolean())
    seeking_description = db.Column(db.String(200))
    date_created = db.Column(db.DateTime(), default=datetime.datetime.utcnow())
    shows = db.relationship('Show', backref='artist', lazy=True)
    
    def __str__(self):
        return f'Name:{self.name}'

    # TODO: implement any missing fields, as a database migration using Flask-Migrate


class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    show_time = db.Column(db.DateTime(), nullable=False)
 
    def __str__(self):
        return f'Name:{self.name}'
# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
