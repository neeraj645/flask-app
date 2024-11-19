from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
  return "this is a webpage of flask app"

if __name__=="__main__":
  app.run(debug=True)