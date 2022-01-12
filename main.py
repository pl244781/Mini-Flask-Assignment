from flask import Flask
import logging

app = Flask(__name__)

ini = [-3, 3]

@app.route('/')
def hello():
  content_list = open('myapp.log', 'r').readlines()
  if ini[0] < len(content_list):
    ini[0] += ini[1]
    if ini[0] + ini[1] < len(content_list):
      return "<br>".join(content_list[ini[0]:ini[0] + ini[1]])
    else:
      return "<br>".join(content_list[ini[0]])
      ini[0] += 1
  else:
    return "Code has finished." 

if __name__ == "__main__":
  logging.basicConfig(filename='myapp.log', level=logging.INFO)
  app.run(host='0.0.0.0', port='5000')
