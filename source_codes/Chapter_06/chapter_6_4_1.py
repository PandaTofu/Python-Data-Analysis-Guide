import pandas as pd

ser1 = pd.Series([0, 1, 2])

ser2 = pd.Series([3, 4])

ser1.append(ser2)

ser1.append(ser2, ignore_index=True)

ser3 = pd.Series([5, 6, 7])

ser1.append([ser2, ser3], ignore_index=True)

ser2})

ser3})

df1.append(df2, ignore_index=True)

