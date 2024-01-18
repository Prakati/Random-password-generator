from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            passcode_length = int(request.form['passcode_length'])
            if passcode_length <= 0:
                raise ValueError("Passcode length must be greater than zero.")
            generated_passcode = generate_password(passcode_length)
            return render_template('index.html', password=generated_passcode)
        except ValueError as e:
            return render_template('index.html', error=str(e))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
