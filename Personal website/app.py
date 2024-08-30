from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Ensure the folder exists
    if not os.path.exists('submissions'):
        os.makedirs('submissions')
    
    # Create a filename based on the name and email
    filename = os.path.join('submissions', f"{name.replace(' ', '_')}_{email.replace('@', '_at_')}.txt")
    
    # Write the form data to a file
    with open(filename, 'w') as file:
        file.write(f"Name: {name}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Message: {message}\n")
    
    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True)
