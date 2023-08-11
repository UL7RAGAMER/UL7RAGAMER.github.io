from flask import Flask, render_template, request

app = Flask(__name__)

# Simulated database of users and passwords (for demonstration purposes)
users = {
    'alice': 'password123',
    'bob': 'securepass',
    'charlie': 'letmein'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            with open('welcome.txt', 'r') as file:
                welcome_message = file.read()
            return welcome_message
        else:
            return "Login failed. Invalid username or password."

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
