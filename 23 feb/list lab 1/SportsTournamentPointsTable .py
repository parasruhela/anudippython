# Example list of team points
points = [45, 60, -10, 75, 30, 60, -5, 90]

print("Original Points:", points)

# 1. Replace negative points with 0
updated_points = [p if p >= 0 else 0 for p in points]

print("After Replacing Negative Points:", updated_points)

# 2. Sort leaderboard (descending order)
sorted_points = sorted(updated_points, reverse=True)

print("Sorted Leaderboard:", sorted_points)

# 3. Find winner and runner-up
if len(sorted_points) >= 2:
    winner = sorted_points[0]
    runner_up = sorted_points[1]
    print("Winner Points:", winner)
    print("Runner-up Points:", runner_up)
else:
    print("Not enough teams to determine winner and runner-up.")