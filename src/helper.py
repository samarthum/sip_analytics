import pandas as pd
import os
import calendar

from src import config


def clean_column_names(df):
    df.columns = ['_'.join(col.lower().split()) for col in df.columns]
    return df


def read_file(path):
    df = pd.read_excel(os.path.join(config.DATA_PATH, path),
                       skiprows=4, engine='openpyxl')
    df = clean_column_names(df)
    return df


def clean_payment_mode(x):
    if x != 'CASH':
        return 'CHEQUE'
    return x


def add_datetime_cols(df, dt_col):
    df.loc[:, dt_col] = pd.to_datetime(df[dt_col])
    df.loc[:, 'receipt_month'] = df[dt_col].dt.month.astype(int)
    df.loc[:, 'receipt_year'] = df[dt_col].dt.year.astype(int)
    return df


def student_monthly_dist(df):
    st_cnt_mon = df.groupby(['receipt_month'])['student_name']\
                 .nunique().reset_index()
    st_cnt_mon.loc[:, 'receipt_month'] = st_cnt_mon['receipt_month']\
        .apply(lambda x: calendar.month_abbr[x])

    return st_cnt_mon
