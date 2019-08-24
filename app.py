from flask import Flask, render_template, request, redirect
import quandl
import pandas as pd

app = Flask(__name__)

quandl.ApiConfig.api_key = 'WhnQwzniPKwSm1cALx-L'

data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'close'] }, date = { 'gte': '2018-01-01', 'lte': '2018-12-31' })
data['month'] = data['date'].dt.month

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)