import matplotlib.pyplot as plt
import numpy as np

students = ['S1','S2','S3','S4','S5','S6']
subjects = ['Math', 'Science','English','History','Art']
months = ['July','Aug','Sep','Dec','Feb']

np.random.seed(42)

math_scores = np.random.randint(60,100,len(students))
science_scores = np.random.randint(55,95,len(students))
english_scores = np.random.randint(70,98,len(students))
history_scores = np.random.randint(65,92,len(students))
art_scores = np.random.randint(75,99,len(students))

student_progress = np.random.randint(60,95,len(months))

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

# Bar Chart (ax1) - Average scores by subject
ax1.set_title('Average scores by subject', fontsize=14, fontweight='bold')
ax1.set_xlabel('Subjects', fontsize=12)
ax1.set_ylabel('Average scores', fontsize=12)

avg_math_scores = np.mean(math_scores)
avg_science_scores = np.mean(science_scores)
avg_english_scores = np.mean(english_scores)
avg_history_scores = np.mean(history_scores)
avg_art_scores = np.mean(art_scores)

averages = [avg_math_scores, avg_science_scores, avg_english_scores, avg_history_scores, avg_art_scores]
bar_colors = np.random.rand(len(subjects), 3)
ax1.bar(subjects, averages, color=bar_colors)
ax1.grid(axis='y')

# Pie Chart (ax2) - Student S1's score distribution
student_index = 0
s1_scores = [math_scores[0], science_scores[0], english_scores[0], history_scores[0], art_scores[0]]

max_score_index = np.argmax(s1_scores)
explode = [0, 0, 0, 0, 0]
explode[max_score_index] = 0.1

ax2.pie(s1_scores, labels=subjects, explode=explode, autopct='%1.1f%%', shadow=True)
ax2.set_title("Student S1's Score Distribution", fontsize=14, fontweight='bold')

# Line Chart (ax3) - Monthly progress
ax3.set_title('Monthly Progress', fontsize=14, fontweight='bold')
ax3.set_xlabel('Months', fontsize=12)
ax3.set_ylabel('Scores', fontsize=12)
ax3.grid(True)
ax3.plot(months, student_progress, marker='o', linestyle='--', linewidth=2, markersize=8)

# Scatter Plot (ax4) - Math vs Science performance
ax4.set_title('Math vs Science Performance', fontsize=14, fontweight='bold')  # Fixed typo
ax4.set_xlabel('Math Scores', fontsize=12)
ax4.set_ylabel('Science Scores', fontsize=12)

# Create colors for scatter plot and add labels
colors = np.random.rand(len(students), 3)
ax4.scatter(math_scores, science_scores, color=colors, s=100)

# Add student labels to each point
for i, student in enumerate(students):
    ax4.annotate(student, (math_scores[i], science_scores[i]), 
                 xytext=(5, 5), textcoords='offset points', fontsize=10)

ax4.grid(True)

plt.tight_layout()
plt.show()