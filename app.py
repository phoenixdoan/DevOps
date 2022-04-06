from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

estimate_list= [{"request":"200 200"}]
@app.route('/')
def index():
    return render_template('index.html', pageTitle="Vertical Tank Maintenance")

@app.route('/about')
def about():
    return render_template('about.html',pageTitle="About VTM")

@app.route('/estimate')
def estimate():
    return render_template('estimate.html',pageTitle="Tank Painting Estimate", values = estimate_list)

@app.route('/generate_estimate', methods=['GET', 'POST'])
def generate_estimate():
    if request.method =='POST':
        form = request.form
        Radius = form['Radius']
        Height = form['Height']
        print(Radius)
        print(Height)
        estimate_dictionary = {"request": Radius + " " + Height}
        print(estimate_dictionary)
        estimate_list.append(estimate_dictionary)
        print(estimate_list)
        return redirect(url_for('estimate'))
    return redirect(url_for('estimate'))







if __name__ == '__main__':
    app.run(debug=True)