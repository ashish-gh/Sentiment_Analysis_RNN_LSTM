from flask import Flask, render_template, flash, request, url_for, redirect, session
import numpy as np
import pandas as pd
import re
import os
from numpy import array


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template("home.html")

