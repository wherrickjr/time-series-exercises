import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def prepare_store(df):
    '''
    this function converts date column to datetime type and makes it the index
    '''
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    df['sale_total'] = df['sale_amount'] * df['item_price']
    df = df.set_index('sale_date')
    df = df.sort_index()
    
    return df


def plot_store(df):
    graph1 = sns.histplot(df['sale_amount'])
    graph2 = sns.histplot(df['item_price'])
    return graph1, graph2