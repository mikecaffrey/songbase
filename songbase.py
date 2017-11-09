from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # return HTML
    # return "<h1>this is the index page!<h1>"
    return "<h1>this is me</h1>"

@app.route('/songs')
def get_all_songs():
    songs = [
        'song 1'
        'song 2'
        'song 3'
    ]
    return render_template ('songs.html', songs=songs)


@app.route('/user/<string:name>/')
def get_user(name):
    return render_template('user.html', user_name=name)


# https://goo.gl/Pc39w8 explains the following line
if __name__ == '__main__':
    app.run(debug=True)

    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)
