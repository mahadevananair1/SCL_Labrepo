
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
division = ['EC', 'CS', 'ME', 'CIVIL', 'B-ARCH']
students = [130,70,190,130,40]
ax.bar(division,students)
plt.show()
