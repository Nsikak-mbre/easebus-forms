#!/usr/bin/env python3

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from .import db
import json

# Create a Blueprint instance for the 'views' module
views = Blueprint("views", __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    """
    Home route where users can view and add notes.
    This view function handles both GET and POST requests.
    
    POST:
        - Retrieves a new note from the form.
        - Validates the length of the note.
        - Adds the new note to the database if validation passes.
    
    GET:
        - Renders the home page with the current user context.
        
    Returns:
        - Renders the 'home.html' template with the user context.
    """
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')  # Error message for short notes
        else:
            new_note = Note(data=note, user_id=current_user.id)  # Create a new note
            db.session.add(new_note)  # Add the note to the database session
            db.session.commit()  # Commit the changes to the database
            flash('Note added!', category='success')  # Success message

    return render_template('home.html', user=current_user)  # Render the home template


@views.route('/delete-note', methods=['POST'])
def delete_note():
    """
    Deletes a note based on the ID received from a JSON request.
    
    POST:
        - Receives a JSON object containing the noteId.
        - Retrieves the note from the database based on the ID.
        - Deletes the note if it belongs to the current user.
    
    Returns:
        - A JSON response after deleting the note.
    """
    note = json.loads(request.data)  # Expecting JSON data from the client-side
    noteId = note['noteId']  # Extract the note ID from the JSON data
    note = Note.query.get(noteId)  # Retrieve the note from the database by ID
    if note:
        if note.user_id == current_user.id:  # Ensure the note belongs to the current user
            db.session.delete(note)  # Delete the note
            db.session.commit()  # Commit the deletion to the database

    return jsonify({})  # Return an empty JSON response
