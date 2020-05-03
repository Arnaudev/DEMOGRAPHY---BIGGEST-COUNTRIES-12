import pandas as pd 
import numpy as np
from numpy.random.tests import data


def main():
    # read CSV files
    df_population_by_country = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_988606.csv', usecols=['Country Name', 'Country Code', '2017'])
    df_population_by_country.columns = ['Country', 'Country Code', 'Population']

    df_country_surface = pd.read_csv('API_AG.SRF.TOTL.K2_DS2_en_csv_v2_989331.csv', usecols=['Country Name', 'Country Code', '2017'])
    df_country_surface.columns = ['Country', 'Country Code', 'Surface']

    # Merge data into a single DataFrame
    df = pd.merge(df_population_by_country, df_country_surface, how='outer', on=['Country', 'Country Code'])

    # Computes density and World surface share
    df['Density'] = df['Population']/df['Surface']

    world = df['Surface'].sum()
    df['World Share'] = df['Surface']/world

    # Filter top 10
    df_top_10 = df.nlargest(10, 'Population')
    print(df_top_10)

if __name__ == "__main__":
    main()