from flask import render_template
from phase3 import app

#server/findings
@app.route("/findings")
def findings():
    title = "Charts"
    template_vars = {
      "title": title
    }
    return render_template("findings.html",vars=template_vars)
