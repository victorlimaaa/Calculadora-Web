from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        operation = request.form.get('operation')
        x = float(request.form.get('x'))
        y = float(request.form.get('y'))

        if operation == 'add':
            result = x + y
        elif operation == 'subtract':
            result = x - y
        elif operation == 'multiply':
            result = x * y
        elif operation == 'divide' and y != 0:
            result = x / y
        elif operation == 'exponential':
            result = x ** y
        else:
            result = 'Invalid operation'

        return render_template('index.html', result=result)
    except ValueError:
        return render_template('index.html', result='Invalid input')

if __name__ == '__main__':
    app.run(debug=True, port=80, host="0.0.0.0")
