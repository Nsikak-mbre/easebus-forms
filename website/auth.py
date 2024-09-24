#!/usr/bin/env python3


from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   # from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user

# Blueprint for authentication routes
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle the login of a user.

    If a POST request is made, checks the user's credentials:
    - If the email exists and the password is correct, the user is logged in.
    - Otherwise, an error message is flashed.
    
    Returns:
        On successful login: Redirect to home page.
        Otherwise: Render the login template with error messages.
    """
    if request.method == 'POST':
        # Get form data
        email = request.form.get('email')
        password = request.form.get('password')

        # Query for the user by email
        user = User.query.filter_by(email=email).first()

        # Check if user exists and password is correct
        if user:
            if check_password_hash(user.password, password):
                # Log in the user
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))  # Redirect to home page
            else:
                # Incorrect password
                flash('Incorrect password, try again.', category='error')
        else:
            # Email does not exist
            flash('Email does not exist.', category='error')

    # Render the login page
    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    """
    Log out the current user.
    
    Requires the user to be logged in. After logging out, the user is redirected 
    to the login page.
    
    Returns:
        Redirect to login page after logout.
    """
    # Log out the current user
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """
    Handle the sign-up of a new user.

    If a POST request is made, validates the form data:
    - Checks if the email already exists.
    - Ensures password meets length and confirmation criteria.
    - If valid, creates a new user and logs them in.
    
    Returns:
        On successful sign-up: Redirect to home page.
        Otherwise: Render the sign-up template with error messages.
    """
    if request.method == 'POST':
        # Get form data
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Query for the user by email
        user = User.query.filter_by(email=email).first()

        # Validate the form data
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            # Create new user with hashed password
            new_user = User(
                email=email,
                first_name=first_name,
                password=generate_password_hash(password1, method='pbkdf2:sha256')
            )

            # Add new user to the database
            db.session.add(new_user)
            db.session.commit()

            # Log in the new user
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))  # Redirect to home page

    # Render the sign-up page
    return render_template("sign_up.html", user=current_user)
