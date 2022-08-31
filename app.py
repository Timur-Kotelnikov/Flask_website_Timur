import flask
app = flask.Flask(__name__)


@app.route('/')
def welcome_page():
    return flask.render_template('welcome_page.html')


@app.route('/general_info')
def general_info():
    return flask.render_template('general_info.html')


@app.route('/education')
def education():
    return flask.render_template('education.html')


@app.route('/job_experience')
def job_experience():
    return flask.render_template('job_experience.html')


@app.route('/hobbies')
def hobbies():
    return flask.render_template('hobbies.html')


if __name__ == '__main__':
    app.run(debug=True)