cat datasets/world_coordinates.csv | head -5

df_coor = pd.read_csv('datasets/world_coordinates.csv', usecols=[1,2])

df_coor.tail()

df_coor['latitude'] = df_coor['latitude'].apply(np.abs)

df_avgTemp = df['2000'].mean().reset_index()

df_avgTemp

df_avgTemp.columns = ['Country', 'avgTemp']

df_avgTemp

df_avgTemp_lat = pd.merge(df_avgTemp, df_coor, on='Country')

df_avgTemp_lat

df_avgTemp_lat.set_index('Country', inplace=True)

df_avgTemp_lat

