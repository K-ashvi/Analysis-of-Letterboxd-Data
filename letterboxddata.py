import pandas as pd
import matplotlib.pyplot as plt

print("Script started.")
path = r"C:\Users\kashv\Downloads\letterboxd data\diary.csv"
df = pd.read_csv(path)
print("CSV file loaded successfully.")
print(df.head(5))  # Display the first 5 rows for better visibility

# Convert 'Watched Date' column to datetime format
df['Watched Date'] = pd.to_datetime(df['Watched Date'], format='%d-%m-%Y')

# Check if the conversion was successful
if df['Watched Date'].isnull().any():
    print("There were issues converting 'Watched Date' to datetime.")

# Add 'weekday' column
df['weekday'] = df['Watched Date'].dt.weekday

# Set our categorical and define the order so the days are plotted Monday-Sunday
df['weekday'] = pd.Categorical(df['weekday'], categories=[0, 1, 2, 3, 4, 5, 6], ordered=True)

# Create df_by_day and count the rows for each weekday, assigning the result to that variable
df_by_day = df['weekday'].value_counts()

# Sort the index using our categorical, so that Monday (0) is first, Tuesday (1) is second, etc.
df_by_day = df_by_day.sort_index()

# Optional: update the font size to make it a bit larger and easier to read
plt.rcParams.update({'font.size': 22})

# Plot df_by_day as a bar chart with the listed size and title
plt.figure(figsize=(20, 10))
df_by_day.plot(kind='bar', title='What Day do I watch movies the most')
plt.xlabel('Day of the Week')
plt.ylabel('Count')
plt.show()  # Show the plot

# Plot ratings
plt.figure(figsize=(20, 10))
df['Rating'] = pd.Categorical(df['Rating'])
df_by_rating = df['Rating'].value_counts().sort_index()
df_by_rating.plot(kind='bar', title='How have i Rated These movies')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()  # Show the plot

# Plot years
plt.figure(figsize=(20, 10))
df_by_year = df['Year'].value_counts().sort_index()
df_by_year.plot(kind='bar', title='What Year are these movies from')
plt.xlabel('Year')
plt.ylabel('Count')
plt.show()  # Show the plot

# Plot tags
# Split the tags and count the occurrences
tags_series = df['Tags'].dropna().str.split(',').explode().str.strip()
df_by_tags = tags_series.value_counts().sort_values(ascending=False)

# Plot df_by_tags as a bar chart with the listed size and title
plt.figure(figsize=(20, 10))
df_by_tags.plot(kind='bar', title='Who have i watched these with')
plt.xlabel('Tags')
plt.ylabel('Count')
plt.show()  # Show the plot

##########################

# Average Rating by Year
plt.figure(figsize=(20, 10))
average_rating_by_year = df.groupby('Year')['Rating'].mean().sort_index()
average_rating_by_year.plot(kind='bar', title='Average Rating by Year')
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.show()

# Movies Watched per Month
plt.figure(figsize=(20, 10))
df['Month'] = df['Watched Date'].dt.month
movies_watched_per_month = df['Month'].value_counts().sort_index()
movies_watched_per_month.plot(kind='bar', title='Movies Watched per Month')
print(df.head())
plt.xlabel('Month')
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

