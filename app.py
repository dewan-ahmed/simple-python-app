from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello Harness!"

@app.route('/redirect')
def unsafe_redirect():
    target = request.args.get('target', '/')
    return redirect(target)

if __name__ == '__main__':
    app.run(debug=True)
