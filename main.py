from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def test():

    cars = {'Audi': 50000,
            'Ford': 30000,
            'BMW': 60000,
            'Toyota': 35000}

    return render_template('index.html', cars = cars)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True)