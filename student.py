import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
num_student = 100
mean_score = 70
std_dev = 10

score = np.random.normal(mean_score, std_dev, num_student)

mean = np.mean(score)
median = np.median(score)
std_dev = np.std(score)
print(f"mean:{mean:.2f},median:{median:.2f},standard deviation:{std_dev:.2f}")
plt.figure(figsize=(10, 6))
sns.histplot(score, bins=10, kde=True, color="blue")
plt.axvline(mean, color="red", linestyle="--", label=f"mean:{mean:.2f}")
plt.axvline(median, color="green", linestyle="-", label=f"median:{median:.2f}")
plt.title("Distribution of student Scores")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.legend()

plt.show()
