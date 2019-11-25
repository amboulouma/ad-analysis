from datetime import date
import decimal

import pandas as pd
import numpy as np
from tqdm import tqdm

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