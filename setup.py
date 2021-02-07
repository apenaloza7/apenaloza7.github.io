from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "If you're reading this, please give me a job!! a_penalo@uncg.edu"

if __name__ == "__main__":
    app.run()
