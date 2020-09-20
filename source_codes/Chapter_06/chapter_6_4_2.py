pd.concat([ser1, ser2])

pd.concat([df1, df2])

pd.concat([df1, df2], axis='columns')

try:
    pd.concat([df1, df2], verify_integrity=True)
except ValueError as e:
    print("ValueError", e)

pd.concat([df1, df2], ignore_index=True)

pd.concat([df1, df2], keys=['data1', 'data2'])

import numpy as np

df1 = pd.DataFrame(np.zeros((3, 3)), columns=['a', 'b', 'c'])

df2 = pd.DataFrame(np.ones((3, 3)), columns=['b', 'c', 'd'])

df1

df2

pd.concat([df1, df2])

pd.concat([df1, df2], join='inner')

