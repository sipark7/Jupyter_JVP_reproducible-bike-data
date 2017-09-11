import os
import pandas as pd
from urllib.request import urlretrieve

FREEMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

def get_fremont_data(filename='freemont-data.csv', url=FREEMONT_URL, force_download=False):
    """Download and cache the freemont data

    Parameters
    ----------
    filename : string(optional)
        location to save the data in csv format
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force download of data

    Returns
    -------
    data : pandas.DataFrame
        The freemont bike bridge data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(URL, 'freemont-data.csv')
    data = pd.read_csv('freemont-data.csv', index_col='Date', parse_dates=True)
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']
    return data
