from flask import Flask
import random
app = Flask(__name__)

random_number = random.randint(0, 9)


def h1_decorator(function):
    def wrapper():
        return '<h1>' + function() + '</h1>'
    return wrapper


@app.route('/')
@h1_decorator
def home():
    return 'Guess a number between 0 and 9'\
        '<br />'\
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def number(number):
    if number > random_number:
        return 'Too high. Guess again' \
            '<br />'\
            '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif number < random_number:
        return 'Too low. Guess again' \
            '<br />'\
            '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return 'correct' \
            '<br />'\
            '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)
