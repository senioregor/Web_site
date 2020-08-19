# -*- coding: utf-8 -*-
from flask import render_template
from flask import request
import warnings
from app import app
import numpy as np
import pandas as pd

warnings.simplefilter('ignore')
import matplotlib.pyplot as plt, mpld3
from pylab import rcParams
import csv

@app.route('/')
@app.route('/index')
def index():
       return render_template('base.html', title='Home')

@app.route('/dataset', methods=['GET', 'POST'])
def dataset():
    from_file = pd.read_csv('zoo.csv', delimiter=',')
    fig, ax = plt.subplots()
    fig1, ax1 = plt.subplots()
    ax.plot([from_file['work_id'], from_file['coin_world']])
    ax1.plot([from_file['work_id'], from_file['coin_my']])
    html_text = mpld3.fig_to_html(fig)
    html_text1 = mpld3.fig_to_html(fig1)
    if request.method == 'POST':
        projectfile = request.form['projectFile']
        aqwer = request.form['aqwer']
        qwerty = request.form['qwerty']
        workid = request.form['workid']
        dict_ = [{'name_work': projectfile, 'coin_world': aqwer, 'coin_my': qwerty,'work_id': workid}]
        from_file = pd.read_csv('zoo.csv', delimiter=',')
        from_form = pd.DataFrame(dict_)
        r = from_file.append(dict_)
        r.to_csv('zoo.csv', sep=',', index=False)

    return render_template('dataset.html', data=from_file.to_html(), htmltext = html_text, htmltext1 = html_text1)

@app.route('/fotoot')
def fotoot():


    return render_template('fotoot.html', title='Foto')


@app.route('/scree')
def screee():
    from_file = pd.read_csv('zoo.csv', delimiter=',')
    fig, ax = plt.subplots()
    fig1, ax1 = plt.subplots()
    ax.plot([from_file['work_id'], from_file['coin_world']])
    ax1.plot([from_file['work_id'], from_file['coin_my']])
    html_text = mpld3.fig_to_html(fig)
    html_text1 = mpld3.fig_to_html(fig1)
    return render_template('script.js', htmltext1=html_text1)