
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "here will be my upload interface"
@app.route("/prepare")
def prepere():
  return render_template(
    'prepare.html',
    invitation="the only limit is yourseff"
)
if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=True)
