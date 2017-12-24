import pandas as pd





data = pd.read_csv('data/data.csv')

liberals = data[data['Party'] == 'Liberal']
ndp = data[data['Party'] == 'NDP']
conservatives = data[data['Party'] == 'Conservative']
