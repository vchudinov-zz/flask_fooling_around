from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("base.html")

@app.route('/ticket')
    def submit_ticket():
        return render_template("ticket.html")
