import pandas as pd

# Moscow
latitude = 55.751244
longitude = 37.618423


def get_default_data():
    df_default = pd.read_csv("default_data_frame.csv")
    numeric_cols = list(df_default.select_dtypes(include=['number']).columns)
    for idx, row in df_default.iterrows():
        for col in numeric_cols:
            if col == 'lat':
                df_default.loc[idx, col] = latitude
            if col == 'lon':
                df_default.loc[idx, col] = longitude
            if col == 'total_square':
                df_default.loc[idx, col] = 75
            if col == 'rooms':
                df_default.loc[idx, col] = 3
            if col == 'floor':
                df_default.loc[idx, col] = 34
            if col == 'is_studio':
                df_default.loc[idx, col] = False
            if col == 'floor_category':
                df_default.loc[idx, col] = 2
    return df_default
