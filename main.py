#!/usr/bin/env python3

from website import create_app

# Create an instance of the Flask application by calling the factory function
app = create_app()

if __name__ == '__main__':
    """
    Entry point for running the Flask application.
    
    When this script is run directly, the Flask development server will start with `debug=True` enabled, allowing for automatic reloading and detailed error messages during development.
    """
    app.run(debug=True)  # Run the Flask app in debug mode
