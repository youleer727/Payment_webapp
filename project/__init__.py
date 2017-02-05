#project/__init__.py

from flask import Flask, request, render_template, session, send_file, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from project.config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)

db = SQLAlchemy(app)

from project.model import User


@app.route('/')
def home():
  return app.send_static_file("index.html")

@app.route('/api/register', methods=['POST'])
def register():
    json_data = request.json
    print json_data
    user = User(        
        password=json_data['password'],
        username=json_data['username']
    )
    try:
        db.session.add(user)
        db.session.commit()
        status = 'success'
        print status
    except:
        status = False
    db.session.close()
    return jsonify({'result': status})

@app.route('/api/login', methods=['POST'])
def login():
    json_data = request.json
    user = User.query.filter_by(password=json_data['password']).first()
    if user.username == json_data['username'] and user.password == json_data['password']:
        session['logged_in'] = True
        status = True
    else:
        status = False
    return jsonify({'result': status})


@app.route('/api/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'result': 'success'})


@app.route('/api/status')
def status():
    if session.get('logged_in'):
        if session['logged_in']:
            return jsonify({'status': True})
    else:
        return jsonify({'status': False})