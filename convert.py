

import pandas as pd

# from pandas.io.json import json_normalize
from pathlib import Path
import json

# set path to file
p = Path(r'C:\Users\HP\Desktop\Data\Data.json')

# read json
with p.open('r', encoding='utf-8') as f:
    data = json.loads(f.read())

# create dataframe
df = pd.json_normalize(data)

# save to csv
df.to_csv('test.csv', index=False, encoding='utf-8')




    


           