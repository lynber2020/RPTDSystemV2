from flask import Flask, render_template


app = Flask(__name__)

TASKS = [
  {
    'id': 1,
    'title': 'Search Owner'    
  },
  {
    'id': 2,
    'title': 'Create Forms'
  },
  {
    'id': 3,
    'title': 'Edit Form'
  }

]
@app.route("/")
def hello_world():
  return render_template('home.html',
                         task=TASKS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
