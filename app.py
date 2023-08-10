import csv

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap

from form import CafeForm

app = Flask(__name__)
SECRET_KEY = 'someRandomKey'
CSV_PATH = './static/cafe-data.csv'
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(app)


def read_from_csv():
    """Read cafes data from the CSV file and return as a list of dictionaries."""
    list_of_rows = []
    with open(CSV_PATH, newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        headers = next(csv_data)
        for row in csv_data:
            list_of_rows.append(dict(zip(headers, row)))
    return list_of_rows


def write_to_csv(data):
    """Append a new cafe entry to the CSV file."""
    with open(CSV_PATH, newline='', mode='a') as csv_file:
        csv_file.write(",".join(data) + "\\n")


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    """Render the form to add a new cafe and handle its submission."""
    form = CafeForm()
    if form.validate_on_submit():
        data = [
            form.cafe.data,
            form.location_url.data,
            form.open_time.data,
            form.close_time.data,
            form.coffee_rating.data,
            form.wifi_rating.data,
            form.power_rating.data
        ]
        write_to_csv(data)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    """Render the page displaying all cafes."""
    cafes_data = read_from_csv()
    return render_template('cafes.html', cafes=cafes_data)


if __name__ == '__main__':
    app.run(debug=True)
