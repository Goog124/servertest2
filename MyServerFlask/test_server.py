from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('index.html', **param)


@app.route('/training/<prof>')
def training(prof):
    param = {}
    param['prof'] = prof
    print(url_for('static', filename='img/mars.jpg'))
    return render_template('training.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')