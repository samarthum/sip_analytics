import pandas as pd
import os
from datetime import datetime
from pathlib import Path

PATH = Path(os.getcwd())
DATA_PATH = os.path.join(PATH, 'data')


def clean_column_names(df):
    """
        Splits the column names on the space (' ') and joins
        them with '_' in order to make it easier to use.
    """
   
    df.columns = ['_'.join(col.lower().split()) for col in df.columns]
    return df


def read_file(path, skiprows=0):
    """
        Function to simplify the reading of files. Uses the DATA_PATH
        in order to fetch the files from the right
        folder.
    """
    if path.endswith('.xlsx'):
        df = pd.read_excel(os.path.join(DATA_PATH, path),
                           skiprows=skiprows, engine='openpyxl')
        
    if path.endswith('.csv'):
        df = pd.read_csv(os.path.join(DATA_PATH, path))
        
    df = clean_column_names(df)
    return df


def str_to_datetime(date_str):
    """
       Converts string object to datetime object. In case null, returns None. 
    """
    if date_str is None:
        return None
    
    return datetime.strptime(date_str, '%d-%m-%Y')


def categorise_duration(months):
    """
        Buckets float month value into string categories like '<2 months', 
        '2-4 months', etc.
    """
    MAX_COURSE_DURATION = 45
    
    for i in range(0, MAX_COURSE_DURATION, 2):
        if (months > i) and (months <= i+2):
            return f'{i if i>=10 else "0" + str(i)}-{i+2 if i+2>=10 else "0" + str(i+2)} months'