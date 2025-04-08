from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# Home page route
@app.route('/')
def index():
    return render_template('index.html')


# Contact form route - handles both GET and POST
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Here you would typically save to a database or send an email
        print(f"New message from {name} ({email}): {message}")

        # Redirect to success page
        return redirect(url_for('success'))

    # If GET request, show the form
    return render_template('contact.html')


# Success page route
@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run()