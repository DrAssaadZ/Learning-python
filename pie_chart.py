import matplotlib.pyplot as plt

labels = 'Python', 'JavaEE', 'PHP', 'JavaScript', 'C++', 'Ruby'
sizes = [20, 85, 80, 30, 10, 5]
separated = (0, 0.1, 0, 0, 0, 0)

plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=separated)
plt.title("usage of programming languages")

plt.show()