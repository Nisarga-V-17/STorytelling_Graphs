import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_excel("student_scores.xlsx")

# Bar Chart
plt.figure()
plt.bar(data["Student"], data["Marks"])
plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Pie Chart
plt.figure()
plt.pie(data["Marks"], labels=data["Student"], autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()

# Histogram
plt.figure()
plt.hist(data["Marks"], bins=5)
plt.title("Marks Distribution Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()