
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json
from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def index():
    
    def create_plot():
        
        labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
        values = [4500, 2500, 1053, 500]
        
        data = [
        go.Pie(labels=labels, values=values, hole=.3, pull=[0, 0, 0.2, 0])
       ]
        
        graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
        
        return graphJSON
    
    
    bar = create_plot()
    
    return render_template('plots.html', plot=bar)
        
    

if __name__ == '__main__':
    app.run(debug=True)