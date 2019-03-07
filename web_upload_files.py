import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

# указываем папку, в которую будут загружаться файлы
UPLOAD_FOLDER = 'D:/Program Files/Uploaded files'
# указываем допустимые расширения
ALLOWED_EXTENSIONS = set(['txt', 'fb2'])

# указываем класс name, чтобы фласк понимал, с чем мы работаем
app = Flask(__name__)
# указываем фласку на папку, заданную нами ранее
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# проверяем соответствует ли расширение файла разрешенным
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# указываем url который будет вызывать функцию, в нашем случае это стартовая страница "/"
@app.route('/', methods=['GET', 'POST'])
# request method  POST нужен для того чтобы загружать файлы
def upload_file():
    if request.method == 'POST':
        # указываем что такое file, у нас file это то, что сайт запрашивает у юзера
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # сохраняем в выбранную папку под оригинальным именем 'filename'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return '''<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <title>File uploaded</title>
</head>
<body>
<div class="alert alert-success"><font size="4" color="black" face="cursive">File successfully uploaded!</font></div>'''
    return '''
            <!doctype html>
            <title>Upload new File (</title>
            <h1>Upload new File (FB2 or TXT, FB2 more preferred)</h1>
            <form method=post enctype=multipart/form-data>
              <input type=file name=file>
              <input type=submit value=Upload>
            </form>
            '''

app.run()
