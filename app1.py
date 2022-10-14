import sqlite3
from turtle import st
from flask import Flask, render_template, url_for, request, redirect, session, flash
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy



@app.route('/')
def index():
    return render_template('resume.html')


if __name__ == "__main__":
    app.run(debug=True)
