from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def query_add():
    """Add a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    sum = add(a, b)

    return str(sum)

@app.route('/sub')
def query_sub():
    """Subtract a from b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    diff = sub(a, b)

    return str(diff)

@app.route('/mult')
def query_mult():
    """Multiply a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    product = mult(a, b)

    return str(product)

@app.route('/div')
def query_div():
    """Divide a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    quot = div(a, b)

    return str(quot)

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<operation>')
def calculate(operation):
    """Calculate opeartion on a and b"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[operation](a, b)

    return str(result)