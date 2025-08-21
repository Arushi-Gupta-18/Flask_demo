from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "sample_secret_key_123"  # Fake secret key for sessions

# Sample sensitive info (dummy data)
SAMPLE_USERNAME = "testuser"
SAMPLE_PASSWORD = "password123"
API_KEY = "FAKE_API_KEY_ABC123XYZ"
SERVER_IP = "192.168.0.10"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == SAMPLE_USERNAME and password == SAMPLE_PASSWORD:
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")


@app.route("/home")
def home():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("home.html", user=session["username"])


@app.route("/secrets")
def secrets():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template(
        "secrets.html",
        api_key=API_KEY,
        server_ip=SERVER_IP
    )


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
