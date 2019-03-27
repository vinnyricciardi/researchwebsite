# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
import pandas as pd

df_links = pd.read_csv("cv_sankey_links.csv")
df_nodes = pd.read_csv("cv_sankey_nodes.csv")

py.sign_in('ID', 'API KEY')

trace1 = {
  "domain": {
    "x": [0, 1], 
    "y": [0, 1]
  }, 
  "link": {
    "label": df_links['link_label'], 
    "labelsrc": "vinnyricciardi:111:0f8d72", 
    "source": df_links['source'], 
    "sourcesrc": "vinnyricciardi:111:e35511", 
    "target": df_links['target'], 
    "targetsrc": "vinnyricciardi:111:d8427c", 
    "value": df_links['link_value'], 
    "valuesrc": "vinnyricciardi:111:a312e7",
    "color": "#f6f5f3"
  }, 
  "node": {
    "label": df_nodes['node_label'], 
    "labelsrc": "vinnyricciardi:111:8bc9cf", 
    "color": "#7dce94",
    "line": {
      # "color": "#35362F", 
      "width": 0.0
    }, 
    "pad": 5, 
    "thickness": 30
  }, 
  "orientation": "h", 
  "type": "sankey", 
  "valueformat": ".0f"
}
data = Data([trace1])
layout = {
  "font": {"size": 10}, 
  "height": 500
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='CV_Sankey')
