from flask import Flask, redirect
import control

app = Flask(__name__)
app.debug = True


@app.route("/")
def index():
    return """
        <a href="/go_forward">Forward</a><br />
        <a href="/go_backward">Backward</a><br />
        <a href="/stop">Stop</a><br />
    """

@app.route("/go_forward")
def go_forward():
    control.go_forward()
    return redirect("/")


@app.route("/go_backward")
def go_backward():
    control.go_backward()
    return redirect("/")


@app.route("/stop")
def stop():
    control.stop()
    return redirect("/")


if __name__ == '__main__':
    app.run(host="0.0.0.0")
