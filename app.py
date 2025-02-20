from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}, 
    'Densi': {'age': 40, 'country': 'Schland'}, 
}

@app.route('/')
def index():
    """
    Displays the homepage and optionally greets the user 
    based on the 'name' query parameter in the URL. Defaults to 'No Name' if not provided.
    """
    user = request.args.get('name', 'No Name')
    return render_template('index.html', user=user, title='Index', weather="good")


@app.route('/greet/<name>')
def greet(name):
    """
    Takes a 'name' from the URL and displays a greeting with the capitalized version of the name.
    """
    name = name.title()
    return render_template('index.html', title='Greetings for all!', user=name)


@app.route('/form')
def form():
    """
    Renders a form page where the user can submit data (e.g., updating user information).
    """
    return render_template('form.html', title='Greetings from Flask')


@app.route('/all-users')
def all_users():
    """
    Displays a list of all users (name, age, and country) from the 'users' dictionary.
    """
    return render_template('all-users.html', users=users, title='All Users')


@app.route('/all-users/table')
def all_users_table():
    """
    Displays a table representation of all users from the 'users' dictionary.
    """
    return render_template('all-users-table.html', users=users, title='All Users Table')


@app.route('/header')
def add_header():
    """
    Website Logo for maximum consistency
    """
    return render_template('header.html')

@app.route('/footer')
def add_footer():
    """
    Website Navigation for maximum consistency
    """
    return render_template('footer.html')


@app.route('/update-country', methods=['GET', 'POST'])
def update_country():
    """
    Allows updating a user's country. If the user exists, updates the country, 
    otherwise adds the user with the provided country without age. 
    Redirects to the 'all_users' route after updating.
    """
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        if name in users:
            users[name]['country'] = country
        else:
            users[name] = {'age': None, 'country': country}
        return redirect(url_for('all_users'))

    return render_template('update-country.html', title='Update Country')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


@app.route('/header.html')
def header():
    return render_template('header.html')

@app.route('/footer.html')
def footer():
    return render_template('footer.html')



if __name__ == "__main__":
    """
    Launches the Flask application on the development server.
    The server listens on port 5000 and is configured for debugging.
    """
    app.run(host="0.0.0.0", port=4000, debug=True)