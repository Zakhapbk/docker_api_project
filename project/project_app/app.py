#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request

app = Flask(__name__)

client= app.test_client()

emploees = [
    {
        'id': 1,
        'name': 'Gregory',
        'position': 'Developer'

    },
    {
        'id': 2,
        'name': 'Kate',
        'position': 'HR'

    }
]




@app.route('/')
def Hello():
    return 'Hello'


@app.route('/emploees/', methods=['GET'])
def base_get():
    return jsonify(emploees)

@app.route('/emploees/',methods=['POST'])
def base_post():
    another = request.json
    emploees.append(another)
    return jsonify(emloees) 



@app.route('/user/<user_id>/')
def user_profile(user_id):
    return "Profile page of user'{}'".format(user_id)

@app.route('/support/')
def sup():
    return "If you have questions or suggestions write on zakhar_z@bk.ru"

if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0', port=5000)
