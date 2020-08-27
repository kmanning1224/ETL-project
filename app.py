import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import and_, or_
from os import environ, path

from flask import Flask, jsonify
from dateutil.relativedelta import *
app = Flask(__name__)
Base = automap_base()
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:////Users/katma/Documents/GitHub/Trilogoy/Homework/etl-project/save_unemployment.db")

# reflect an existing database into a new model

# reflect the tables
Base.prepare(engine, reflect=True)

Base.classes.keys()
# Save references to each table
print
# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################


@app.route("/")
def welcome():
    
    """List all available api routes."""
    return (
        f"Available Climate API Routes:<br/></br></br>"
        f"Follow this for information Stations: </br></br>"
        f"/api/v1.0/stations</br></br>"
        f"Follow this for information on Precipitation: </br></br>"
        f"/api/v1.0/precipitation</br></br>"
        f"Follow this for information Temperature: </br></br>"
        f"/api/v1.0/tobs</br></br>"
        f"Follow this to review set Start date averages: </br></br>"
        f"/api/v1.0/temp/<start></br></br>"
        f"Follow this for a set start and end date average: </br></br>"
        f"/api/v1.0/temp/<start>/<end></br></br>"
    )

#Convert the query results to a dictionary using date as the key and prcp as the value.

#Return the JSON representation of your dictionary.
# 
if __name__ == '__main__':
    app.run(debug=True)
