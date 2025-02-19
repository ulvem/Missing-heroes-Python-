from data import movies

# You can use the `movies` array here
# Please write every correction and modification of the data to this file by updating the `movies` array

# WRITE YOUR CODE HERE
from data import movies

# Loop through each movie in the movies array
for movie in movies:
    # Check if the director key has an empty string
    if movie.get('director') == '':
        # Update the director to Martin Scorsese
        movie['director'] = 'Martin Scorsese'

# Print the updated movies array to verify the changes
print(movies)

# Loop through each movie in the movies array
for movie in movies:
    # Check if the year is incorrect (less than 1900)
    if movie['year'] < 1900:
        # Add 1000 or 2000 to correct the year
        if movie['year'] < 900:
            movie['year'] += 2000
        else:
            movie['year'] += 1000

# Print the updated movies array to verify the changes
print(movies)

# Loop through each movie in the movies array
for movie in movies:
    # Check if Leonardo da Vinci is mistakenly listed as an actor
    if 'Leonardo da Vinci' in movie.get('actors', []):
        # Replace Leonardo da Vinci with Leonardo DiCaprio
        movie['actors'] = ['Leonardo DiCaprio' if actor == 'Leonardo da Vinci' else actor for actor in movie['actors']]

# Print the updated movies array to verify the changes
print(movies)

# Loop through each movie in the movies array
for movie in movies:
    # Check if 'Drama' is missing and there are no empty strings in the genres list
    if 'Drama' not in movie.get('genres', []):
        # Add 'Drama' to the genres list
        movie['genres'].append('Drama')

# Print the updated movies array to verify the changes
print(movies)

# Initialize a list to store all actors
all_actors = []

# Loop through each movie in the movies array
for movie in movies:
    # Add the actors from each movie to the all_actors list
    all_actors.extend(movie.get('actors', []))

# Count all actors without worrying about duplicates
allTheActors = len(all_actors)

# Print the total number of actors
print(f"Total number of actors (including duplicates): {allTheActors}")

# Optional: Count unique actors by converting the list to a set
unique_actors = set(all_actors)
unique_actors_count = len(unique_actors)

# Print the total number of unique actors
print(f"Total number of unique actors: {unique_actors_count}")

