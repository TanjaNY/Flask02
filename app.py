from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        radius = float(request.form['radius'])
        area = round(3.14159 * radius ** 2, 2)
        return render_template('index.html', radius=radius, result=area)
    except ValueError:
        return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
