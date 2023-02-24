import pandas as pd

text = '''

    username:{username}
    email:{email}
    address:{address}
    title:{title}
    salary:{salary}

'''
def create_email(row_num):
    df = pd.read_csv('user_data.csv')

    username = df.iloc[row_num][1]
    email = df.iloc[row_num][2]
    address = df.iloc[row_num][3]
    title = df.iloc[row_num][4]
    salary = df.iloc[row_num][5]

    print(text.format(username = username, email = email, address = address, title = title, salary = salary))

row = 174

create_email(row-2)