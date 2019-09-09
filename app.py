from flask import Flask, render_template, request
from for_ex import draw_certs
from a18irepl import randomize_companies

app = Flask(__name__)
app.config["DEBUG"] = True

for_ex_draw_nb_times = 0


@app.route("/")
def main(error="", success=""):
    return render_template("main.html", error=error, success=success)


@app.route("/", methods=["POST"])
def main_post():
    global for_ex_draw_nb_times;
    error = ""

    if "for_ex_draw_certs_submit" in request.form:
        success = draw_certs()
        for_ex_draw_nb_times += 1
        print("-----USED-----   FOR EX   draw certificates ({0} times [might be incorrect])".format(for_ex_draw_nb_times))
        return main(error=error, success=success)

    elif "18irepl_randomize_companies_submit" in request.form:
        success = randomize_companies()
        return main(error=error, success=success)

    return main(error=error)

