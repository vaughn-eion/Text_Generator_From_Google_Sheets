import google_connector as gc
import pandas as pd
from datetime import date

cols = ['Username', 'Email', 'Address', 'Title', 'Salary']

def save_data(data):
    df = pd.DataFrame(data, columns=cols)
    df = df.tail(-1)
    df.to_csv(f'user_data.csv')

save_data(gc.gather_data())