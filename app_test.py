'''

from config import create_app, db

app = create_app()

with app.app_context():
    db.create_all()

import uuid
from flask import Flask, request, make_response, render_template, redirect, url_for, Response, send_from_directory, jsonify, session, flash
import pandas as pd
import os


@app.route('/', methods=['GET', 'POST', 'FILE'])
def index():
    response = make_response("Hello World")
    response.status_code= 202
    response.headers['content-type']= 'application/json'
    return response

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if 'username' in request.form.keys() and 'password' in request.form.keys():
            return 'success'
        return 'not in form keys'

    name = 'Ines'
    mylist = [i for i in range(10, -1, -1)]
    return render_template('indexe.html', name=name, mylist=mylist, message='Index')

@app.route('/file', methods=['POST'])
def file():
    file = request.files.get('file')

    if file.content_type == 'text/plain':
        return file.read().decode()

    if file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        df = pd.read_excel(file)
        return df.to_html()
    return 'a'

@app.route('/convert_file_two', methods=['POST'])
def convert_file_two():
    file = request.files.get('file')
    df = pd.read_excel(file)

    if not os.path.exists('downloads'):
        os.makedirs('downloads')


    filename = f'file_{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads', filename))

    return render_template('download.html', filename=filename)


@app.route('/download/<filename>', methods=['GET','POST'])
def download(filename):
    return send_from_directory('downloads', filename, download_name='result.csv')


@app.route('/greet/<name>', methods=['GET', 'POST'])
def ines(name):
    if request.method == 'POST':
        return 'This is a post request'
    return f'Hello {name}'


@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'{number1} + {number2} = {number1 + number2}'


@app.route('/handle_url_params')
def handle():
    if 'name' in request.args.keys() and 'age' in request.args.keys():
        name = request.args.get('name')
        age = request.args.get('age')
        return f'My name is {name} and I am {age} years old'
    return 'no parameters'


@app.route('/filters')
def filters():
    text= 'ines'
    return render_template('filters.html', text=text)


@app.route('/redirect')
def redirect_url():
    return redirect(url_for('filters'))


@app.route('/handle_post', methods=['POST'])
def handle_post():
    greeting = request.json['greeting']
    name = request.json['name']
    with open('downloads/file.txt', 'w') as file:
        file.write(f'{greeting}, {name}')

    return jsonify({'message' : 'successfully written'})


@app.route('/set_data')
def set_data():
    session['name'] = 'Ines'
    session['age'] = 32
    return render_template('indexe.html', message='Session set')

@app.route('/get_data')
def get_data():
    message = 'no session found'
    if 'name' in session.keys() and 'age' in session.keys():
        name = session['name']
        age = session['age']
        message = f'{name}, {age}'
    return render_template('indexe.html', message=message)


@app.route('/erase_data')
def erase_data():
    session.clear()
    return render_template('indexe.html', message='Erased data')


@app.route('/set_cookie')
def set_cookie():
    response = make_response(render_template('indexe.html', message='set cookie'))
    response.set_cookie('name', 'ines')
    return response

@app.route('/get_cookie')
def get_cookie():
    value = "no cookie"
    if 'name' in request.cookies.keys():
        value= request.cookies.get('name')
    return render_template('indexe.html', message=value)

@app.route('/erase_cookie')
def erase_cookie():
    response = make_response(render_template('indexe.html', message='set cookie'))
    response.delete_cookie('name')
    return response


@app.route('/login', methods=['POST', 'GET'])
def login():
    name = request.form.get('username')
    password = request.form.get('password')
    message='coucou'

    if name and password:
        message='allo'
        session['name'] = name
        flash('Vous êtes connecté', 'success')
    return render_template('indexe.html', message=message)


@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]


@app.template_filter('repeat')
def repeate(s, times=5):
    return (s + ' ') * times


@app.template_filter('alternate_case')
def alternate_case(s):
    return ''.join([letter.upper() if index % 2 == 0 else letter.lower() for index, letter in enumerate(s)])

'''
