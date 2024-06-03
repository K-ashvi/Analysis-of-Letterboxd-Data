import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
path = r"C:\Users\kashv\Downloads\letterboxd data\diary.csv"
df = pd.read_csv(path)
print("CSV file loaded successfully.")
#displaying columns
print(df.head()) 

# Convert 'Watched Date' column to datetime format
df['Watched Date'] = pd.to_datetime(df['Watched Date'], format='%d-%m-%Y')

# Add 'weekday' column
df['weekday'] = df['Watched Date'].dt.weekday

# define the order so the days are plotted Monday-Sunday
df['weekday'] = pd.Categorical(df['weekday'], categories=[0, 1, 2, 3, 4, 5, 6], ordered=True)

# count the rows for each weekday
df_by_day = df['weekday'].value_counts()

# Sort the days
df_by_day = df_by_day.sort_index()

# change the font size 
plt.rcParams.update({'font.size': 15})

# plot
plt.figure(figsize=(20, 10))
df_by_day.plot(kind='bar', title='What Day Do I Watch Movies The Most?')
plt.xlabel('Day of the Week')
plt.ylabel('Count')
plt.show()  

# Plot ratings
plt.figure(figsize=(20, 10))
df['Rating'] = pd.Categorical(df['Rating'])
df_by_rating = df['Rating'].value_counts().sort_index()
df_by_rating.plot(kind='pie', title='How Have I Rated These Movies?')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show() 

# Plot years starting from 1970
# Plot years
years = np.arange(1970, df['Year'].max() + 1)
df_years = pd.DataFrame(index=years, columns=['Count'])
df_by_year = df['Year'].value_counts().sort_index()
df_years['Count'] = df_by_year
plt.figure(1, figsize=(20, 10)) 
plt.plot(df_years.index, df_years['Count'], marker='o', linestyle='-')
plt.title('What Year Are These Movies From?')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()



# Plot tags
# Split the tags and count the occurrences
tags_series = df['Tags'].dropna().str.split(',').explode().str.strip()
df_by_tags = tags_series.value_counts().sort_values(ascending=False)
plt.figure(figsize=(20, 10))
df_by_tags.plot(kind='bar', title='Who Have I Watched These With?')
plt.xlabel('Tags')
plt.ylabel('Count')
plt.show()  


# Average Rating by Year
# Convert 'Rating' column to numeric data type
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
# Calculate average rating by year
average_rating_by_year = df.groupby('Year')['Rating'].mean().sort_index()
plt.figure(figsize=(20, 10))
average_rating_by_year.plot(kind='bar', title='Average Rating by Year')
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.show()

# Movies Watched per Month
plt.figure(figsize=(20, 10))
df['Month'] = df['Watched Date'].dt.month
movies_watched_per_month = df['Month'].value_counts().sort_index()
movies_watched_per_month.plot(kind='bar', title='Movies Watched per Month')
plt.xlabel('Month')
plt.ylabel('Count')
plt.show()

# Movies Watched per Year
plt.figure(figsize=(20, 10))
df['Watched Year'] = df['Watched Date'].dt.year
df['Watched Year'].value_counts().sort_index().plot(kind='bar', title='Movies Watched per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()

# Average Rating by Day of the Week
plt.figure(figsize=(20, 10))
average_rating_by_day = df.groupby('weekday')['Rating'].mean().sort_index()
average_rating_by_day.plot(kind='bar', title='Average Rating by Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Average Rating')
plt.xticks(range(7), ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.show()

#most watched
movie_counts = df['Name'].value_counts()
watched_more_than_once = movie_counts[movie_counts > 1]
plt.figure(figsize=(20, 10))
watched_more_than_once.plot(kind='bar', title='My Most Watched')
plt.xlabel('Movie Name')
plt.ylabel('Count')
plt.show()

