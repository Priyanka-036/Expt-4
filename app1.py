
from flask import Flask, render_template, url_for




@app.route('/')
def index():
    return render_template('resume.html')


if __name__ == "__main__":
    app.run(debug=True)
