from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ["GET","POST"])
def index():
  #post
  if request.method == "POST":
    message = request.form["message"]
    with open("messages.txt","a") as f1:
      f1.write(message + "\n")
    return render_template("index.html", message=message)
  #get
  with open("messages.txt","r") as file:
    posts = file.readlines()  
  print(posts)
  return render_template("index.html",posts=posts)
    

app.run(host='0.0.0.0', port=81)
