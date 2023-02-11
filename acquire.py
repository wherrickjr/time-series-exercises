#standard ds imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#imports
import os
import requests
import datetime
from env import username, host, password


######################## Get SQL Connection Function #########################


def get_connection(db, user=username, host=host, password=password):
    
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    
########################## Planet Acquire and CSV Function ####################

def get_planet_data():
    '''
    This function creates a csv of planet data if one does not exist
    if one already exists, it uses the existing csv 
    and brings it into pandas as dataframe
    '''
    if os.path.isfile('planet.csv'):
        df = pd.read_csv('planet.csv', index_col=0)
    
    else:
        response = requests.get('https://swapi.dev/api/planets/')
        data = response.json()
        df = pd.DataFrame(data['results'])
        while data['next'] != None:
            print(data['next'])
            response = requests.get(data['next'])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
        df.to_csv('planet.csv')

    return df


###################### Starships Acquire and CSV Function ####################

def get_starships_data():
    '''
    This function creates a csv of starship data if one does not exist
    if one already exists, it uses the existing csv 
    and brings it into pandas as dataframe
    '''
    if os.path.isfile('starships.csv'):
        df = pd.read_csv('starships.csv', index_col=0)
    
    else:
        response = requests.get('https://swapi.dev/api/starships/')
        data = response.json()
        df = pd.DataFrame(data['results'])
        while data['next'] != None:
            print(data['next'])
            response = requests.get(data['next'])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
        df.to_csv('starships.csv')

    return df



####################### People Acquire and CSV Function #######################

def get_people_data():
    '''
    This function creates a csv of people data if one does not exist
    if one already exists, it uses the existing csv 
    and brings it into pandas as dataframe
    '''
    if os.path.isfile('people.csv'):
        df = pd.read_csv('people.csv', index_col=0)
    
    else:
        response = requests.get('https://swapi.dev/api/people/')
        data = response.json()
        df = pd.DataFrame(data['results'])
        while data['next'] != None:
            print(data['next'])
            response = requests.get(data['next'])
            data = response.json()
            df = pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
        df.to_csv('people.csv')

    return df


######################## Germany Acquire and CSV Function ####################

def get_germany_data():
    '''
    This function creates a csv of germany energy data if one does not exist
    if one already exists, it uses the existing csv 
    and brings it into pandas as dataframe
    '''
    if os.path.isfile('opsd_germany_daily.csv'):
        df = pd.read_csv('opsd_germany_daily.csv', index_col=0)
    
    else:
        url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'
        df = pd.read_csv(url)
        df.to_csv('opsd_germany_daily.csv')

    return df

###################### Store Acquire and CSV Function ####################

def get_store_data():
    '''
    This function looks for a csv file,
    if the file has not already been create, 
    it pulls the query from sql, saves it to a csv for future use
    and returns a pandas dataframe using that query.
    ''' 
    filename = 'store.csv'  
    if os.path.exists(filename):    
        return pd.read_csv(filename)
    
    else: 
        query = '''
                SELECT sale_date, sale_amount,
                item_brand, item_name, item_price,
                store_address, store_zipcode
                FROM sales
                LEFT JOIN items USING(item_id)
                LEFT JOIN stores USING(store_id)
                '''
        url = get_connection(db='tsa_item_demand')
        
        df = pd.read_sql(query, url)
        df.to_csv(filename, index=False)
        
        return df

        ##########################concat dataframe#####################
def combine_everything(x,y,z):
    '''
    this function combines 3 dataframes 
    '''
    df = pd.concat([x,y,z], axis =1)
    return df
            