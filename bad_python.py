import flask

app = flask.Flask(__name__)

@app.route('/')
def insecure():
    expr = flask.request.args.get('expr')
    return str(eval(expr))

if __name__ == '__main__':
    app.run(debug=True)