from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import quandl
import pandas as pd

app = Flask(__name__)

quandl.ApiConfig.api_key = 'WhnQwzniPKwSm1cALx-L'

data = quandl.get_table('WIKI/PRICES', qopts = { 'columns': ['ticker', 'date', 'close'] }, date = { 'gte': '2018-01-01', 'lte': '2018-12-31' })
data['month'] = data['date'].dt.month
tick_names = sorted(data['ticker'].unique())
months = sorted(data['month'].unique())

def create_figure(current_tick_name, current_month):
  df = data[data['ticker'] == current_tick_name]
  data_filtered = df[df['month'] == int(current_month)]
  p = figure(x_axis_type = 'datetime', plot_width=1000, plot_height=500)
  p.line(data_filtered.date, data_filtered.close)
  p.xaxis.axis_label = 'date'
  return p

@app.route('/')
def index():
  current_tick_name = request.args.get("tick_name")
  if current_tick_name == None:
    current_tick_name = "V"
  
  current_month = request.args.get("month")
  if current_month == None:
    current_month = 1

  plot = create_figure(current_tick_name, current_month)
      
  script, div = components(plot)
  return render_template("stock.html", script=script, div=div, tick_names = tick_names, current_tick_name=current_tick_name, months = months, current_month = current_month)

if __name__ == '__main__':
  app.run(port=33507, debug=True)