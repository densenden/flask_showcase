# Flask User Management Application

This is a simple Flask application for managing users. It includes features such as greeting users, displaying user information, and updating user details.

## Features

- **Homepage**: Displays a greeting message based on the user's name provided in the URL.
- **Greet**: Greets the user with a capitalized version of their name.
- **Form**: A form page where users can submit their name.
- **All Users**: Displays a list of all users with their age and country.
- **All Users Table**: Displays a table representation of all users.
- **Update Country**: Allows updating a user's country or adding a new user with a country.

## Routes

- `/`: Displays the homepage and optionally greets the user based on the 'name' query parameter.
- `/greet/<name>`: Greets the user with the capitalized version of their name.
- `/form`: Renders a form page for user input.
- `/all-users`: Displays a list of all users.
- `/all-users/table`: Displays a table of all users.
- `/update-country`: Allows updating a user's country or adding a new user.

## Templates

- `index.html`: Template for the homepage.
- `form.html`: Template for the form page.
- `footer.html`: Template for the footer with route overview.

## Static Files

- `style.css`: CSS file for styling.
- `layout.js`: JavaScript file for layout functionality.


## Running the Application

1. Run the Flask application:
    ```sh
    python app.py
    ```
2. Open your web browser and navigate to `http://localhost:5000`.

## License

This project is licensed under the MIT License.