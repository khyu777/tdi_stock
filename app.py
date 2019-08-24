from flask import Flask, render_template, request, redirect
import quandl
import pandas as pd

app = Flask(__name__)

quandl.ApiConfig.api_key = 'WhnQwzniPKwSm1cALx-L'

data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'close'] }, date = { 'gte': '2018-01-01', 'lte': '2018-12-31' })
data['month'] = data['date'].dt.month

def create_figure(current_tick_name, current_month):
  df = data[data['ticker'] == current_tick_name]
  data_filtered = df[df['month'] == int(current_month)]
  p = figure(x_axis_type = 'datetime', plot_width=1000, plot_height=500)
  p.line(data_filtered.date, data_filtered.close)
  p.xaxis.axis_label = 'date'
  return p

if __name__ == '__main__':
  app.run(port=33507)