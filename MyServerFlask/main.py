from flask import Flask, render_template, url_for
from data import db_session

from data.users import User
from data.jobs import Jobs
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/works')
def table_works():
    db_session.global_init("db/mars_explorer.db")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("works.html", jobs=jobs)


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()