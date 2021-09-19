from flask import Flask, render_template, request, redirect, render_template, send_from_directory
from identicon import Identicon
from os import path

istring = ''

idcon = Identicon(istring)
app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def home():
    check_exist_file = path.isfile(path.join(app.config['FILE_PATH'], app.config['DEFAULT_FILENAME']))

    if istring and check_exist_file:
        title = istring

        return render_template('index.html', image_name=app.config['DEFAULT_FILENAME'], image_title=title)
    else:
        return render_template('index.html')
    

@app.route('/render', methods=['POST'])
def render():
    global istring, save_success, idcon
    save_success = False
    istring = request.form['istring']

    idcon = Identicon(istring)
    idcon.save_image(path.join(app.config['FILE_PATH'], app.config['DEFAULT_FILENAME']))

    return redirect('/')


@app.route('/download', methods=['GET', 'POST'])
def download():
    filename = save()
    full_path = path.join(app.root_path, app.config['FILE_PATH'])

    return send_from_directory(directory=full_path, path=filename)


def save():
    global istring, save_success

    filename = istring + '.png'
    file_path = path.join(app.config['FILE_PATH'], filename)
    idcon.save_image(file_path)

    istring = ''

    return filename