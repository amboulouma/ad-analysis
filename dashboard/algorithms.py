from datetime import date
import decimal

import pandas as pd
import numpy as np
from tqdm import tqdm
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db.utils import OperationalError


from .models import Compaign
from .constants import *
from .utils import *

# Populate the database function
def populate_database(filename):
    Compaign.objects.all().delete()
    csv_data = pd.read_csv(filename)
    for row in tqdm(csv_data.iterrows()):
        if not np.isnan(row[1][4]): 
            date, data_source, compaign_name, clicks, impressions = "-".join(row[1][0].split('.')[::-1]), row[1][1], row[1][2], row[1][3], int(row[1][4])
            Compaign.objects.create(date=date, data_source=data_source, compaign_name=compaign_name, clicks=clicks, impressions=impressions)        

# Query the database function
def query_database(query,type_):
    results, message = None, None
    try:
        if type_ == "date":
            query = "-".join(query.split("/")[::-1])
            results = Compaign.objects.filter(date=query)
        elif type_ == "data_source": results = Compaign.objects.filter(data_source=query)
        elif type_ == "compaign_name": results = Compaign.objects.filter(compaign_name=query)
        elif type_ == "clicks": results = Compaign.objects.filter(clicks=query)
        elif type_ == "impressions": results = Compaign.objects.filter(impressions=query)
        elif type_ == "sql_query": results = Compaign.objects.raw(query)
    except (ValidationError, OperationalError) as e:
        query, results = None, None
        message = "Please enter a valid Value"
    return results, message