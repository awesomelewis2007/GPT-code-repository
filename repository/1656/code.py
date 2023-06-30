import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

class MusicRecommendationSystem:
    def __init__(self, user_data, music_data):
        self.user_data = user_data
        self.music_data = music_data

    def recommend_songs(self, user_id, mood):
        user_history = self.user_data.loc[user_id]
        user_history = user_history[user_history > 0]  # Filter out unplayed songs

        # Calculate user similarity
        similarities = cosine_similarity(self.user_data, self.user_data)
        user_similarity = similarities[user_id]

        # Find similar users
        similar_users = pd.Series(user_similarity).sort_values(ascending=False)[1:]

        # Generate song recommendations
        recommendations = pd.Series()
        for user in similar_users.index:
            user_songs = self.user_data.loc[user]
            user_songs = user_songs[user_songs > 0]  # Filter out unplayed songs

            for song in user_songs.index:
                if song not in user_history.index:
                    if song in recommendations:
                        recommendations[song] += user_similarity[user] * user_songs[song]
                    else:
                        recommendations[song] = user_similarity[user] * user_songs[song]

        # Filter recommendations by mood
        mood_recommendations = self.music_data[self.music_data['mood'] == mood]
        recommendations = recommendations[recommendations.index.isin(mood_recommendations.index)]

        # Sort recommendations by score
        recommendations = recommendations.sort_values(ascending=False)

        return recommendations.head(10)  # Return top 10 recommendations

# Load user listening history data
user_data = pd.read_csv('user_data.csv', index_col=0)

# Load music data
music_data = pd.read_csv('music_data.csv', index_col=0)

# Create music recommendation system
recommendation_system = MusicRecommendationSystem(user_data, music_data)

# Get user input
user_id = input("Enter your user ID: ")
mood = input("Enter your current mood: ")

# Get music recommendations
recommendations = recommendation_system.recommend_songs(user_id, mood)

# Display recommendations
print("Music Recommendations:")
for song in recommendations.index:
    print(song)
