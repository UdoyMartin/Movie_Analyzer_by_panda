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