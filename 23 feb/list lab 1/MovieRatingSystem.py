# Example list of ratings
ratings = [5, 4, 3, 6, 2, 5, 1, 0, 4, 5, -1]

print("Original Ratings:", ratings)

# 1. Remove invalid ratings (valid range: 1–5)
valid_ratings = [r for r in ratings if 1 <= r <= 5]

print("Valid Ratings:", valid_ratings)

# 2. Find average rating
if valid_ratings:
    average_rating = sum(valid_ratings) / len(valid_ratings)
    print("Average Rating:", round(average_rating, 2))
else:
    print("No valid ratings available.")

# 3. Count how many 5-star ratings
five_star_count = valid_ratings.count(5)
print("Number of 5-Star Ratings:", five_star_count)

# 4. Sort ratings in ascending order
sorted_ratings = sorted(valid_ratings)
print("Sorted Ratings (Ascending):", sorted_ratings)