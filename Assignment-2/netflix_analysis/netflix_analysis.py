import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("netflix_titles.csv")


genres = df['listed_in'].str.split(', ').explode()
top_10_genres = genres.value_counts().head(10)

print("\nTop 10 Genres:")
print(top_10_genres)

top_10_genres.plot(kind='bar', title='Top 10 Netflix Genres')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.tight_layout()
plt.show()


type_dist = df['type'].value_counts()

print("\nMovies vs TV Shows:")
print(type_dist)

type_dist.plot(
    kind='pie',
    autopct='%1.1f%%',
    title='Movies vs TV Shows'
)
plt.ylabel('')
plt.show()


df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year

content_per_year = df['year_added'].value_counts().sort_index()

print("\nContent Added Per Year:")
print(content_per_year.tail())

content_per_year.plot(title='Content Added Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.show()


countries = df['country'].dropna().str.split(', ').explode()
top_countries = countries.value_counts().head(10)

print("\nTop Content Producing Countries:")
print(top_countries)

top_countries.plot(kind='bar', title='Top 10 Content Producing Countries')
plt.xlabel('Country')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

print("\nCountry producing most content:")
print(top_countries.idxmax())