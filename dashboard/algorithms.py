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
        date, data_source, compaign_name, clicks = "-".join(row[1][0].split('.')[::-1]), row[1][1], row[1][2], row[1][3]
        if not np.isnan(row[1][4]): impressions = int(row[1][4])
        else: impressions = None
        Compaign.objects.create(date=date, compaign_name=compaign_name, data_source=data_source, clicks=clicks, impressions=impressions)
