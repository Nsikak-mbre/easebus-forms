#!/usr/bin/env python3

from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    """
    This class represents a Note in the database.
    
    Attributes:
        id (int): Primary key for the note.
        data (str): The content of the note, stored as a string.
        date (datetime): Timestamp when the note was created, defaults to the current time.
        user_id (int): Foreign key linking to the user who created the note.
    """
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))  # Note content
    date = db.Column(db.DateTime(timezone=True), default=func.now())  # Timestamp of creation
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Foreign key to User table

class User(db.Model, UserMixin):
    """
    This class represents a User in the database.
    
    Attributes:
        id (int): Primary key for the user.
        email (str): Unique email address of the user.
        password (str): Hashed password for authentication.
        first_name (str): The first name of the user.
        notes (relationship): One-to-many relationship linking to the notes created by the user.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)  # Unique email for the user
    password = db.Column(db.String(150))  # Hashed password for the user
    first_name = db.Column(db.String(150))  # First name of the user
    notes = db.relationship('Note')  # Relationship to notes created by the user
