import pandas as pd

# Generic Text
text = '''

    username:{username}
    email:{email}
    address:{address}
    title:{title}
    salary:{salary}

'''

# Create general text from file 
def create_text(row_num):
    df = pd.read_csv('user_data.csv')

    username = df.iloc[row_num][1]
    email = df.iloc[row_num][2]
    address = df.iloc[row_num][3]
    title = df.iloc[row_num][4]
    salary = df.iloc[row_num][5]

    print(text.format(username = username, email = email, address = address, title = title, salary = salary))

# Input which row of data that will be used to generate the text.
row = 174

create_text(row-2)
