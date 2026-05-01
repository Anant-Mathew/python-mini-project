import pandas as pd
import matplotlib.pyplot as plt

# loading the csv file
df = pd.read_csv("students.csv")

# checking the data
print(df.head())
print(df.shape)

# basic stats
print("Average Marks :", df["Marks"].mean())
print("Max Marks :", df["Marks"].max())
print("Min Marks :", df["Marks"].min())

# average marks by subject
avg_subject = df.groupby("Subject")["Marks"].mean()
print(avg_subject)

# average marks by student
avg_student = df.groupby("Name")["Marks"].mean()
print(avg_student)

# pivot table for heatmap
pivot = df.pivot_table(index="Name", columns="Subject", values="Marks")

# ----- PLOTS -----

fig, axes = plt.subplots(2, 2, figsize=(12, 9))
fig.suptitle("Student Marks Analysis", fontsize=16)

# plot 1 - bar chart subjects
axes[0, 0].bar(avg_subject.index, avg_subject.values, color=["blue", "orange", "green", "red", "purple"])
axes[0, 0].set_title("Avg Marks by Subject")
axes[0, 0].set_xlabel("Subject")
axes[0, 0].set_ylabel("Marks")

# plot 2 - bar chart students
axes[0, 1].bar(avg_student.index, avg_student.values, color=["cyan", "pink", "yellow", "lime", "salmon"])
axes[0, 1].set_title("Avg Marks by Student")
axes[0, 1].set_xlabel("Student")
axes[0, 1].set_ylabel("Marks")

# plot 3 - scatter plot
axes[1, 0].scatter(df["Study_Hours"], df["Marks"], color="blue")
axes[1, 0].set_title("Study Hours vs Marks")
axes[1, 0].set_xlabel("Study Hours")
axes[1, 0].set_ylabel("Marks")

# plot 4 - heatmap (manual using imshow)
im = axes[1, 1].imshow(pivot.values, cmap="YlOrRd", aspect="auto")
axes[1, 1].set_xticks(range(len(pivot.columns)))
axes[1, 1].set_xticklabels(pivot.columns, rotation=30)
axes[1, 1].set_yticks(range(len(pivot.index)))
axes[1, 1].set_yticklabels(pivot.index)
axes[1, 1].set_title("Heatmap - Marks")
fig.colorbar(im, ax=axes[1, 1])

# add numbers inside heatmap cells
for i in range(len(pivot.index)):
    for j in range(len(pivot.columns)):
        axes[1, 1].text(j, i, int(pivot.values[i][j]), ha="center", va="center", fontsize=9)

plt.tight_layout()
plt.savefig("student_analysis_beginner.png", dpi=150)
print("done! saved the chart")
