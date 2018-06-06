from flask import Flask, render_template, request, redirect, send_file, g
import os
import for_ex

app = Flask(__name__)


@app.route("/")
def main(error="", success=""):
    return render_template("main.html", error=error, success=success)


@app.route("/", methods=["POST"])
def main_post():
    error = ""
    if "for_ex_draw_certs_submit" in request.form:
        success = for_ex.draw_certs()
        return main(error=error, success=success)
    return main(error=error)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=88, debug=True)
