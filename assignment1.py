import csv
import pandas as pd

#import files
airports = pd.read_csv('airports.csv', keep_default_na=False)
countries = pd.read_csv('countries.csv',keep_default_na=False)
runways = pd.read_csv('runways.csv',keep_default_na=False)

#get count for the number of airports per country
airport_counts = (
    airports.groupby("iso_country")
    .size()
    .reset_index(name="num_airports")
)

#get longest runway per country
airport_runways = airports.merge(
    runways,
    left_on="ident",
    right_on="airport_ident",
    how="inner"
)

#get the index of the longest runway for each country
idx = airport_runways.groupby("iso_country")["length_ft"].idxmax()
longest_runways = airport_runways.loc[idx][
    ["iso_country", "name", "length_ft", "width_ft"]
].rename(columns={"name": "airport_name"})

#combine the dataframes to get the desired result
result = (
    countries.merge(
        airport_counts,
        left_on="code",
        right_on="iso_country",
        how="left"
    )
    .merge(
        longest_runways,
        on="iso_country",
        how="left"
    )
)

#select and rename the desired columns
results = result[[
    "id", 
    "name", 
    "continent", 
    "num_airports", 
    "airport_name", 
    "length_ft", 
    "width_ft"
    ]].rename(columns={
        "name": "country_name",
        "code": "iso_country"
})

#sort the results by number of airports in descending order
results = result.sort_values(by="num_airports", ascending=False)

#print the first 3 and last 10 rows of the results
print(results.head(3))
print(results.tail(10))
results.to_csv('results.csv', index=False)

