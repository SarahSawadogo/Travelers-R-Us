# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
import os
from flask import redirect



#  worldImageList
# -- Initialization section --
app = Flask(__name__)
# -- Routes section --


@app.route('/')
@app.route('/index.html')



if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
