import pandas as pd
import numpy as np

#step 1: Create Dataframe, find series, data_range

movies = pd.DataFrame({
    "title":        ["Inception", "Titanic", "The Dark Knight", "Avatar",
                     "Interstellar", "Parasite", "The Avengers", "Joker",
                     "Avengers: Endgame", "The Lion King"],
    "genre":        ["Sci-Fi", "Romance", "Action", "Sci-Fi",
                     "Sci-Fi", "Thriller", "Action", "Thriller",
                     "Action", "Animation"],
    "year":         [2010, 1997, 2008, 2009,
                     2014, 2019, 2012, 2019,
                     2019, 2019],
    "rating":       [8.8, 7.9, 9.0, 7.8,
                     8.6, 8.5, 8.0, 8.4,
                     8.4, 6.9],
    "revenue":      [836, 2187, 1005, 2923,
                     773, 258, 1519, 1079,
                     2798, 1663],     # millions USD
    "budget":       [160, 200, 185, 237,
                     165, 11, 220, 55,
                     356, 260],       # millions USD
    "release_date": ["2010-07-16", "1997-12-19", "2008-07-18", "2009-12-18",
                     "2014-11-07", "2019-05-30", "2012-05-04", "2019-10-04",
                     "2019-04-26", "2019-07-19"],
    "director":     ["Nolan", "Cameron", "Nolan", "Cameron",
                     "Nolan", "Bong", "Whedon", "Phillips",
                     "Russo", "Favreau"],
})
print(movies)
print("\n Data Series: \n", pd.Series([8.8, 7.9, 9.0, 7.8], name="rating"))
print("\n Data Range: \n", pd.date_range(start="2010-07-16", end="2014-11-07",freq="YE"))

#step 2: Inspection (head, tail, info, describe, shape, columns, index, dtypes)
print('\nSTEP 2 — Inspection\n')

print('\n Head(3):\n', movies.head(3))
print('\n Tail(3):\n', movies.tail(3))
print('\n Info:', movies.info())
print('\n Describe:\n', movies.describe())
print('\n Shape;', movies.shape)
print('\n Columns:\n', movies.columns.tolist())
print('\n Index:', movies.index)
print('\n Data Types:\n', movies.dtypes)

#step 3: Selection & Indexing (loc, iloc, at, iat, boolean indexing)
print('\n STEP 3 - Selection & Indexing\n')

print('\n df["title"]:\n', movies["title"])
print('\n df["title"]:\n', movies["title"].values)
print('\n df[["title", "genre"]]:\n', movies[["title", "genre"]].to_string())
print('\n df.loc[0:2, "title":"rating"]:\n', movies.loc[0:2, "title":"rating"])
print('\n df.iloc[0:3, 0:4]:\n ', movies.iloc[0:3, 0:4])
print('\n df.at[1, "title"]:', movies.at[1, 'title'])
print('\n df.iat[0,1]:', movies.iat[0,1])

#step 4: Filtering & Boolean Masking (boolean indexing, sort_values, sort_index)
print('\n STEP 4 - Filtering & Boolean Masking\n')

high_rated= movies[movies["rating"]>8.5]
print('\n rating>8.5:\n', high_rated[["title", "rating"]])

nolan_movies=movies[movies["director"].isin(["Nolan", "Cameron"])]
print('\n ,isin(["Nolan", "Cameron"]):\n', nolan_movies[["title", "director"]])

mid_revenue=movies[movies["revenue"].between(800, 2000)]
print('\n revenue between 800 and 2000:\n', mid_revenue[["title", "director", "revenue"]])

top_query=movies.query("rating>8.0 & revenue>1000")
print('\n query(rating>8.0 & revenue>1000): \n', top_query[["title", "rating", "revenue"]])

not_scifi = movies[~(movies["genre"] == "Sci-Fi")]
print("\n not_scifi:\n", not_scifi[["title", "genre"]])

#step 5: handling Missing Data (isnull, notnull, dropna, fillna, isna, sum)
print('\n STEP 5 - Handling Missing Data\n')

movies_nan= movies.copy()
movies_nan.loc[7, "rating"]=np.nan
movies_nan.loc[5, "revenue"]=np.nan
movies_nan.loc[2, "budget"]=np.nan

print('\n isnull():\n', movies_nan.isnull())
print('\n notnull():\n', movies_nan.notnull())
print('\n isna():\n', movies_nan.isna())
print('\n sum():\n', movies_nan.isnull().sum())

movies_nan["budget"]=movies_nan["budget"].fillna(movies_nan["budget"].mean())
print('\n fillna():\n', movies_nan)

cleaned_movies=movies_nan.dropna(subset=["rating", "revenue"])
print('\n dropna():\n', cleaned_movies)

#Step 6: Adding & Modifying Columns( assign, rename, drop, apply, map, applymap)
print('\n STEP 6 - Adding & Modifying Columns\n')

movies["profit"]=movies["revenue"]-movies["budget"]
print('\n Profit column added:\n', movies[["title", "revenue", "budget", "profit"]])

movies["blockbuster"]=movies["revenue"].apply(lambda x: "Yes" if x>1000 else "No")
print("\n Blockbuster column added:\n", movies[["title", "revenue", "blockbuster"]])

grade_map={8.8: "A", 7.9: "B", 9.0: "A+", 7.8: "B-", 8.6: "A", 8.5: "A", 8.0: "B+", 8.4: "A-", 6.9: "C"}
movies["grade"]=movies["rating"].map(grade_map).fillna("C")
print("\n Grade column added:\n", movies[["title", "rating", "grade"]])

movies=movies.assign(roi =lambda x: ((x["revenue"]-x["budget"])/ x["budget"])*100).round(1)
print("\n ROI column added:\n", movies[["title", "revenue", "budget", "roi"]])

movies=movies.rename(columns={"revenue": "revenue_m", "budget": "budget-m"})
print("\n Columns renamed:\n", movies.columns.tolist())

movies=movies.drop(columns=["grade"])
print("\n Columns dropped:\n", movies.columns.tolist())

#step 7: Sorting & Ranking
print('\n STEP 7 - Sorting & Ranking\n')

by_revenue=movies.sort_values(by="revenue_m", ascending=False)
print('\n Sorted by revenue_m:\n', by_revenue[["title", "revenue_m"]].head (5))

print('\n .nlargest(3, rating):\n ', movies.nlargest(3, "rating")[["title", "rating"]])
print('\n .nsmallest(3, rating):\n ', movies.nsmallest(3, "rating")[["title", "rating"]])

movies["revenue_rank"]=movies["revenue_m"].rank(ascending=False)
print('\n Revenue Rank:\n', movies[["title", "revenue_m", "revenue_rank"]])

#step 8 - Groupby & aggregation
print('\n STEP 8 - Groupby & Aggregation \n')

print('\n Group by genre and calculate mean revenue:\n ', movies.groupby("genre")["revenue_m"].mean().round(1))
genre_stats= movies.groupby("genre").agg(
    avg_rating= ("raitng", "mean"),
    total_revenue= ("revenue_m", "sum"),
    movie_count=("title", "count")
),round(1)
print('\n Genre Stats:\n', genre_stats)

movies["genre_avg-revenue"]= movies.groupby("genre")['revenue_m'].transform("mean").round(1)
print('\n Transform genre_avg-revenue:\n', movies[["title", "genre", "revenue_m", "genre_avg-revenue"]])

pivot_table=movies.pivot_table(movies, index="genre", values="revenue_m", columns="blockbuster", aggfunc="mean", fill_value=0)
print('\n Pivot Table:\n', pivot_table)

crosstab= pd.crosstab(movies["genre"], movies["blockbuster"])
print('\n Crosstab ( genre vs blockbuster):\n', crosstab)

