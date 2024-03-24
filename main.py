## Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
url = "https://drive.google.com/uc?id=10oyIT1KPdwUqeU9-2LX0xE5-ZytNn9su"
fifa_players = pd.read_csv(url)

# Display the first five rows of the dataset
print(fifa_players.head())
# Display the last five rows of the dataset
print(fifa_players.tail())
#################################################################################################
# Count the number of players per country
players_per_country = fifa_players['Nationality'].value_counts()

# Get the country with the most number of players
most_players_country = players_per_country.idxmax()
num_players_most_country = players_per_country.max()

print("Country with the most number of players:", most_players_country)
print("Number of players in the most represented country:", num_players_most_country)
#################################################################################################
# Get the top 5 countries
top_5_countries = players_per_country.head()

# Plot bar chart
plt.figure(figsize=(10, 6))
top_5_countries.plot(kind='bar', color='skyblue')
plt.title('Top 5 Countries with the Most Number of Players')
plt.xlabel('Country')
plt.ylabel('Number of Players')
plt.xticks(rotation=45)
plt.show()
#################################################################################################
# Find the player with the highest salary
fifa_players['Wage'] = fifa_players['Wage'].str.replace('€','')
fifa_players['Wage'] = fifa_players['Wage'].str.replace('K','e+3')
fifa_players['Wage'] = pd.to_numeric(fifa_players['Wage'])
highest_salary_player = fifa_players.loc[fifa_players['Wage'].idxmax()]

print("Player with the highest salary:", highest_salary_player['Name'])
print("Salary:", highest_salary_player['Wage'])
#################################################################################################
# Plot histogram of player salaries
plt.figure(figsize=(10, 6))
plt.hist(fifa_players['Wage'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Salary Range of Players')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
#################################################################################################
# Find the tallest player
fifa_players['Height'] = fifa_players['Height'].str.replace("'",'.')
fifa_players['Height'] = pd.to_numeric(fifa_players['Height'])
tallest_player = fifa_players.loc[fifa_players['Height'].idxmax()]

print("Tallest player:", tallest_player['Name'])
print("Height:", tallest_player['Height'])
#################################################################################################
# Count the number of players per club
players_per_club = fifa_players['Club'].value_counts()

# Get the club with the most number of players
most_players_club = players_per_club.idxmax()
num_players_most_club = players_per_club.max()

print("Club with the most number of players:", most_players_club)
print("Number of players in the most represented club:", num_players_most_club)
#################################################################################################
# Count the preferred foot of players
preferred_foot_counts = fifa_players['Preferred Foot'].value_counts()

# Plot bar chart
plt.figure(figsize=(8, 6))
preferred_foot_counts.plot(kind='bar', color='orange')
plt.title('Preferred Foot of Players')
plt.xlabel('Preferred Foot')
plt.ylabel('Number of Players')
plt.xticks(rotation=0)
plt.show()
