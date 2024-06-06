from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number = int(request.form['number'])
        square = number * number
        return render_template('index.html', square=square)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
