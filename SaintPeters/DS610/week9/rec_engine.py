import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# import the data
data = pd.read_csv('data.csv')

# create a user-item matrix
user_item_matrix = data.pivot_table(index='userID', columns='itemID', values='rating')

# calculate cosine similarity
item_similarity = cosine_similarity(user_item_matrix.T)

# make a dataframe out of the item similarity matrix
item_similarity_df = pd.DataFrame(item_similarity, index=user_item_matrix.columns, columns=user_item_matrix.columns)

# get the item co-occurrences
item_cooccurrences = item_similarity_df.dot(item_similarity_df.T)


item_cooccurrences_df = pd.DataFrame(item_cooccurrences, index=user_item_matrix.columns, columns=user_item_matrix.columns)

# get the user's item ratings
user_ratings = user_item_matrix.loc[userID]

# compute the weighted sum of item co-occurrences
weighted_sum = user_ratings.dot(item_cooccurrences_df)

# get the top-k recommendations
top_k_recs = weighted_sum.sort_values(ascending=False).head(k)