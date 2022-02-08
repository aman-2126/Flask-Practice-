import sqlite3
import pandas as pd
import numpy as np
con = sqlite3.connect("students.sqlite")
cur = con.cursor()
data = list()
for row in cur.execute('SELECT * FROM users;'):
    data.append(row[1])
con.close()

# print(data.values)
df = pd.DataFrame(data, columns=["Name"])
x = np.array(df)
print(x)
