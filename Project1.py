import pandas


df = pandas.read_csv("movie_dataset.csv")

df = df.rename(columns = {'Runtime (Minutes)':'Runtime_(Minutes)'})
df = df.rename(columns = {'Revenue (Millions)':'Revenue_(Millions)'})

new_df = df.dropna(subset=['Revenue_(Millions)'], how='all')

new_df = new_df.drop(columns = "Rank")
new_df = new_df.drop(columns = "Description")
new_df = new_df.drop(columns = "Votes")
new_df = new_df.drop(columns = "Metascore")


Highest_rated_movie = new_df.loc[new_df['Rating'].idxmax()]['Title']

print(f"The highest rated movie is: {Highest_rated_movie}")


Revenue = 'Revenue_(Millions)'

Average_revenue = new_df[Revenue].mean()

print(f"The average revenue of all movies is: {Average_revenue} Million")

Year_column = 'Year'

filtered_df = new_df[(new_df[Year_column] >= 2015) & (new_df[Year_column] <= 2017)]

New_Average_revenue = filtered_df[Revenue].mean()

print(f"The average revenue of all movies  between 2015 and 2017 is: {New_Average_revenue} Million")

Target_year = 2016

Movies_in_2016 = df[df[Year_column] == Target_year]

Number_of_movies = Movies_in_2016.shape[0]

print(f"Number of movies released in {Target_year}: {Number_of_movies}")

Director_names = 'Director'
Target_director = 'Christopher Nolan'
Director = df[df[Director_names] == Target_director]
Number_of_directed_movies = Director.shape[0]

print(f"The number of movies directed by '{Target_director}' is: {Number_of_directed_movies}")

Rating_column = 'Rating'

Number_of_movies__atleast_8_rating = filtered_rating.shape[0]

print(f"The number of movies with a rating of atleast 8.0 rating is: {Number_of_movies__atleast_8_rating}")
Median_rating = Director[Rating_column].median()

print(f"The median rating  of all the movies directed by '{Target_director}' is: {Median_rating}")

Average_ratings_by_year = df.groupby('Year')['Rating'].mean()

Highest_avg_rating_year = Average_ratings_by_year.idxmax()

print(f"The year with the highest average rating is: {Highest_avg_rating_year}")


Movies_2006 = df[df['Year'] == 2006]
Movies_2016 = df[df['Year'] == 2016]

Num_Movies_2006 = len(Movies_2006)
Num_Movies_2016 = len(Movies_2016)
Percentage_increase = ((Num_Movies_2016 - Num_Movies_2006) / Num_Movies_2006) * 100
print(f"The percentage increase in the number of movies between 2006 and 2016 is: {Percentage_increase:.2f} %")

Actors_column = 'Actors'
All_names = new_df[Actors_column].str.split(',', expand=True).stack()
Unique_name_counts = All_names.value_counts()

print(Unique_name_counts)
Unique_genres = df['Genre'].unique()

Num_unique_genres = len(Unique_genres)

print(f'The number of unique genres in the dataset is: {Num_unique_genres}')

Correlation_matrix = df.corr()
print(Correlation_matrix)
