import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# YouTube data

categories = np.array([
    "Music", "Gaming", "Education", "Tech", "Comedy",
    "Music", "Gaming", "Education", "Tech", "Comedy"
])

views = np.array([
    50000, 80000, 120000, 200000, 150000,
    90000, 180000, 100000, 250000, 140000
])

likes = np.array([
    5000, 8000, 12000, 20000, 15000,
    9000, 18000, 10000, 25000, 14000
])

comments = np.array([
    500, 800, 1200, 2000, 1500,
    900, 1800, 1000, 2500, 1400
])

# Basic data analysis

print("YouTube Data Analysis")
print("Total Videos:", len(views))
print("Average Views:", np.mean(views))
print("Average Likes:", np.mean(likes))
print("Average Comments:", np.mean(comments))

highest = np.max(views)
print("Highest Views:", highest)

print("\nAverage Views by Category")

average_views = []

for category in np.unique(categories):
    category_views = views[categories == category]
    average = np.mean(category_views)
    average_views.append(average)
    print(category, ":", average)

# 1. Line Chart

plt.plot(views, marker="o")
plt.title("Views of Videos")
plt.xlabel("Video Number")
plt.ylabel("Views")
plt.show()

# 2. Bar Chart

plt.bar(np.unique(categories), average_views)
plt.title("Average Views by Category")
plt.xlabel("Category")
plt.ylabel("Average Views")
plt.xticks(rotation=20)
plt.show()

# 3. Histogram

plt.hist(comments, bins=5)
plt.title("Comments Distribution")
plt.xlabel("Comments")
plt.ylabel("Number of Videos")
plt.show()

# 4. Pie Chart

category_names, category_count = np.unique(
    categories, return_counts=True
)

plt.pie(
    category_count,
    labels=category_names,
    autopct="%1.1f%%"
)
plt.title("Videos by Category")
plt.show()

# 5. Scatter Plot

plt.scatter(views, likes)
plt.title("Views and Likes")
plt.xlabel("Views")
plt.ylabel("Likes")
plt.show()

# 6. Box Plot

sns.boxplot(x=categories, y=views)
plt.title("Views by Category")
plt.xlabel("Category")
plt.ylabel("Views")
plt.xticks(rotation=20)
plt.show()

# 7. Violin Plot

sns.violinplot(x=categories, y=views)
plt.title("Views Distribution by Category")
plt.xlabel("Category")
plt.ylabel("Views")
plt.xticks(rotation=20)
plt.show()

# 8. Heatmap

data = np.array([views, likes, comments])
correlation = np.corrcoef(data)

sns.heatmap(
    correlation,
    annot=True,
    xticklabels=["Views", "Likes", "Comments"],
    yticklabels=["Views", "Likes", "Comments"]
)
plt.title("Correlation Heatmap")
plt.show()

# 9. Count Plot

sns.countplot(x=categories)
plt.title("Number of Videos in Each Category")
plt.xlabel("Category")
plt.ylabel("Number of Videos")
plt.xticks(rotation=20)
plt.show()

# 10. Pair Plot

data_for_pairplot = pd.DataFrame({
    "Views": views,
    "Likes": likes,
    "Comments": comments
})

sns.pairplot(data_for_pairplot)
plt.show()