from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', pageTitle="Vertical Tank Maintenance")


@app.route('/about')
def about():
    return render_template('about.html', pageTitle="About VTM")


@app.route('/estimate')
def estimate():
    return render_template('estimate.html', pageTitle="Tank Painting Estimate", cost_estimate=0, radius=0, height=0)


@app.route('/generate_estimate', methods=['GET', 'POST'])
def generate_estimate():
    if request.method == 'POST':
        form = request.form
        radius = int(form['radius'])
        height = int(form['height'])
        print(radius)
        print(height)
        pi = 3.14
        tank_top = pi * radius * radius
        tank_side = 2 * (pi * (radius * height))
        total_area = tank_top + tank_side
        total_square_feet = total_area/144
        total_mat_cost = total_square_feet * 25.00
        total_labour_cost = total_square_feet * 15.00
        total_cost_estimate = total_mat_cost + total_labour_cost
        return render_template('estimate.html', pageTitle="Tank Painting Estimate",
                               height=height, radius=radius, cost_estimate=round(total_cost_estimate, 2))
    return redirect(url_for('estimate'))


if __name__ == '__main__':
    app.run(debug=True)
