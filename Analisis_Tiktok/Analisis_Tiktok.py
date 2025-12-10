
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("Overview.csv")

# 2. Clean column names
df = df.rename(columns={
    'Video Views': 'views',
    'Profile Views': 'profile_views',
    'Likes': 'likes',
    'Comments': 'comments',
    'Shares': 'shares',
    'Date': 'date'
})

# 3. Convert numeric data
numeric_cols = ['views', 'profile_views', 'likes', 'comments', 'shares']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# 4. Convert date
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# 5. New metrics
df['engagement_count'] = df['likes'] + df['comments'] + df['shares']
df['engagement_rate'] = df['engagement_count'] / df['views'].replace(0, 1)

# 6. Basic stats
print("\n=== Summary statistics ===")
print(df.describe())

# 7. Top videos
print("\n=== Top 5 videos by views ===")
print(df.nlargest(5, 'views')[['date', 'views', 'likes', 'comments', 'shares']])

print("\n=== Top 5 videos by engagement rate ===")
print(df.nlargest(5, 'engagement_rate')[['date', 'views', 'engagement_rate']])

# 8. Correlation matrix
print("\n=== Correlation matrix ===")
print(df[['views', 'likes', 'comments', 'shares', 'engagement_count']]
      .corr())

# 9. Plot 1: Histogram of views
plt.figure(figsize=(8, 5))
plt.hist(df['views'])
plt.title("Distribution of Video Views")
plt.xlabel("Views")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("hist_views.png")

# 10. Plot 2: Likes vs Views
plt.figure(figsize=(8, 5))
plt.scatter(df['views'], df['likes'])
plt.title("Likes vs Views")
plt.xlabel("Views")
plt.ylabel("Likes")
plt.tight_layout()
plt.savefig("scatter_likes_vs_views.png")

print("\nAnalysis finished. Images saved.")
