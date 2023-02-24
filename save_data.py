import google_connector as gc
import pandas as pd

# Columns from google sheets
cols = ['Username', 'Email', 'Address', 'Title', 'Salary']

# Save data from google sheets into local csv so there is not a need to constantly call the api
def save_data(data):
    df = pd.DataFrame(data, columns=cols)
    df = df.tail(-1)
    df.to_csv(f'user_data.csv')

save_data(gc.gather_data())
