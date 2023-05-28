from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! 16"

if __name__ == "__main__":    
    func = None
    try:
        func = request.environ.get('werkzeug.server.shutdown')
    except RuntimeError as re:
        print("no running server")
    if not func is None:
        #raise RuntimeError('Not running with the Werkzeug Server')
        func()    
    app.run(host='0.0.0.0', port=4567)
