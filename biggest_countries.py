import pandas as pd


def main():
    # read CSV files
    df_country_codes = pd.read_csv('countries.csv', usecols=['code', 'country'])
    country_codes = df_country_codes['code'].tolist()

    df_population_by_country = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_988606.csv', usecols=['Country Name', 'Country Code', '2017'])
    df_population_by_country.columns = ['Country', 'Country Code', 'Population']

    df_country_surface = pd.read_csv('API_AG.SRF.TOTL.K2_DS2_en_csv_v2_989331.csv', usecols=['Country Name', 'Country Code', '2017'])
    df_country_surface.columns = ['Country', 'Country Code', 'Surface']

    # Merge data into a single DataFrame
    df = pd.merge(df_population_by_country.loc[df_population_by_country['Country Code'].isin(country_codes)], df_country_surface, how='inner', on=['Country', 'Country Code'])

    # Computes density and World surface share
    df['Density'] = df['Population']/df['Surface']

    # World surface
    world = df_country_surface.loc[df_country_surface['Country'] == 'World', 'Surface'].item()
    print(f'World Surface: {world}')
    print('\n\n')

    df['World Share'] = df['Surface']/world

    # Filter top 10 population
    df_top_10_population = df.nlargest(10, 'Population')
    print(df_top_10_population.to_string(index=False))

    # Filter top 10 surface
    df_top_10_surface = df.nlargest(10, 'Surface')
    print(df_top_10_surface.to_string(index=False))

    # Filter top 10 density
    df_top_10_density = df.nlargest(10, 'Density')
    print(df_top_10_density.to_string(index=False))


if __name__ == "__main__":
    main()
