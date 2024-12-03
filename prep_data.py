import pandas as pd 

earthquake_data = "earthquake_data.csv"
gdp_data_earthquakes = "gdp-world-regions-stacked-area.csv"
population_data = "P_Population_and_GDP_by_Country/36791fff-eb5f-420b-9492-c6b5490b9db2_Data.csv"
population_metadata = "P_Population_and_GDP_by_Country/36791fff-eb5f-420b-9492-c6b5490b9db2_Series-Metadata.csv"

def read_files(file):
    # what is the sybtax for the utf encoding?
    df = pd.read_csv(file)
    return df 

def count_na(df):
    '''counts the null values of each column in a given df'''
    return df.isnull().sum()

def remove_high_na_columns(df, threshold=2500):
    # Identify columns with null values exceeding the threshold
    high_na_columns = df.columns[df.isnull().sum() > threshold]
    # Drop those columns from the DataFrame
    return df.drop(columns=high_na_columns)



def main():
    eq_df= read_files(earthquake_data)
    # print(eq_df.columns)
    # print(eq_df['Location Name'].tail())
    # eq_df_filtered = eq_df[eq_df[['Year', 'Mo', 'Dy', 'Hr', 'Mn', 'Sec', 'Tsu', 'Vol', 'Location Name']]]
    # print(eq_df)
    gdp_df= read_files(gdp_data_earthquakes)
    # print("gdp df", gdp_df)
    # check how to keep the rest of the df 
    gdp_df['Entity']= gdp_df['Entity'].str.upper()

    # why are there more rows now with a left join when the left df orginally had 3918 rows and not theres 456540
    merged = pd.merge(
    eq_df,
    gdp_df,
    left_on=['Location Name', 'Year'],  # Columns from eq_df
    right_on=['Entity', 'Year'],       # Columns from gdp_df
    how="left")
    # print(merged)
    # print(count_na(merged))
    # new_merged = remove_high_na_columns(merged, threshold=2500)
    # print(new_merged)
    pop_file = "population/population.csv"
    pop_df= read_files(pop_file)
    pop_df["Entity"] = pop_df["Entity"].str.upper()
    print(pop_df)
    merged2 = pd.merge(
    merged,
    pop_df,
    left_on=['Location Name', 'Year'],  # Columns from eq_df
    right_on=['Entity', 'Year'],       # Columns from gdp_df
    how="left")
    # print(merged2)
    # print(count_na(merged2))
    new_merged = remove_high_na_columns(merged2, threshold=2500)
    # print(new_merged)
    new_merged = new_merged.drop(columns=['Entity_x','Entity_y', 'Code_y'])
    new_merged = new_merged.rename(columns={
    'Location Name': 'Country Name',
    'Location Original': 'Original Country Name',
    'Code_x':'Country Code'
    })
    print(new_merged)
    new_merged.to_csv('earthquake_merged.csv')
    # pop_df= read_files(population_data)
    # print(pop_df)why
    # pop_meta_df= read_files(population_metadata)
    # print(pop_meta_df)

main()