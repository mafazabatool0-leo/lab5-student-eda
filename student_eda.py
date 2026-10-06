import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "StudentID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    "Gender": [
        "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Female"
    ],
    "StudyHours": [5, 3, 6, 4, 7, 2, 8, 3, 6, 4, 7, 5],
    "Attendance(%)": [90, 82, 92, 85, 95, 78, 96, 80, 88, 83, 91, 89],
    "Marks": [82, 68, 88, 72, np.nan, 65, 91, 70, np.nan, 75, 84, 79]
}

df = pd.DataFrame(data)

duplicate_row = df.iloc[[10]]

df = pd.concat([df, duplicate_row], ignore_index=True)

df.to_csv("student_performance.csv", index=False)

df = pd.read_csv("student_performance.csv")

print("Shape:", df.shape)

print("\nDataset Information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

df["Marks"] = df["Marks"].fillna(df["Marks"].median())

print("\nAfter cleaning:", df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())

plt.figure(figsize=(6, 4))
plt.hist(df["Marks"], bins=6, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.savefig("marks_histogram.png")
plt.show()

plt.figure(figsize=(5, 4))
plt.boxplot(df["Marks"])
plt.title("Marks Boxplot")
plt.ylabel("Marks")
plt.savefig("marks_boxplot.png")
plt.show()

plt.figure(figsize=(6, 4))
plt.scatter(df["StudyHours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("studyhours_vs_marks.png")
plt.show()

correlation_matrix = df[
    ["StudyHours", "Attendance(%)", "Marks"]
].corr()

print("\nCorrelation matrix:")
print(correlation_matrix)

gender_summary = df.groupby("Gender")[
    ["Marks", "Attendance(%)"]
].mean()

print("\nAverage Marks and Attendance by Gender:")
print(gender_summary)

print("\nSaved marks_histogram.png")
print("Saved marks_boxplot.png")
print("Saved studyhours_vs_marks.png")