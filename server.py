#!/usr/bin/env python
from flask import Flask, jsonify

__info = {
    'name': 'Erik Lonroth',
    'skill': 100,
    'title': 'wizard'
}

info = __info

application = Flask(__name__)

@application.route('/')
def index():
    return "Online"

# Show info
@application.route('/api/info', methods=['GET'])
def get_info():
    return jsonify(info)


def main():
    application.run()

if __name__ == '__main__':
    application.run()
