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
    return render_template('training.html', **param)


@app.route('/list_prof/<list>')
def list_prof(list):
    data_prof = ["Инженер", "Строитель", "Медик", "Повар", "Пилот"]
    param = {}
    param['list'] = list
    param['prof_list'] = data_prof
    return render_template('list_prof.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')