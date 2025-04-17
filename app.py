from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        mode = request.form["mode"]
        form_data = {k: float(request.form[k]) for k in request.form if k != "mode"}

        if mode == "monthly":
            return render_template("results.html", result=calculate_monthly(form_data))
        else:
            return render_template("results.html", result=calculate_yearly(form_data))

    return render_template("index.html")

def calculate_monthly(data):
    the_rest = sum([
        data["Gas"], data["Bills_Utilities"], data["Education"], data["Entertainment"],
        data["Personal"], data["Home"]
    ])

    csp = 1.25 * ((data["Travel"] * 0.02) + (data["Dining"] * 0.03) + (the_rest * 0.01)) - (45 / 12)
    csr = 1.5 * ((data["Travel"] + data["Dining"]) * 0.03 + the_rest * 0.01) - (250 / 12) - ((data["Authorized_Users"] * 75) / 12)

    return {
        "better_card": "CSP" if csp > csr else "CSR",
        "monthly_csp": round(csp, 2),
        "monthly_csr": round(csr, 2)
    }

def calculate_yearly(data):
    the_rest = sum([
        data["Gas"], data["Bills_Utilities"], data["Education"], data["Entertainment"],
        data["Personal"], data["Home"], data["Groceries"], data["Shopping"]
    ])

    csp = 1.25 * ((data["Travel"] * 0.02) + (data["Dining"] * 0.03) + (the_rest * 0.01)) - 45
    csr = 1.5 * ((data["Travel"] + data["Dining"]) * 0.03 + the_rest * 0.01) - 250 - (data["Authorized_Users"] * 75)

    return {
        "better_card": "CSP" if csp > csr else "CSR",
        "yearly_csp": round(csp, 2),
        "yearly_csr": round(csr, 2)
    }

if __name__ == "__main__":
    app.run(debug=True)
