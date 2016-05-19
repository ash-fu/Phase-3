from flask import Flask, render_template
from routes import *
import buildhtml
import codecs
app = Flask(__name__, static_folder='.', static_url_path='')

<<<<<<< HEAD

@app.route("/")
def index():
    f = codecs.open("./templates/frontpage_try.html", "w")
    html = buildhtml.dropdown("data_2012.csv")
    f.write(html)
    f.close()
    return render_template("frontpage_try.html")

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=2525)



