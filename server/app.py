#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5000, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_hello(parameter):
    print(parameter)
    return parameter

@app.route('/count/<parameter>')
def count(parameter):
    return '\n'.join(str(i) for i in range(int(parameter))) + '\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math_operation(num1, operation, num2):
    num1, num2 = int(num1), int(num2)
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == '/':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Invalid operation'
    