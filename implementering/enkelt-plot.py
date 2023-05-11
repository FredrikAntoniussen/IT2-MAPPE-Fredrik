import matplotlib.pyplot as plt


x = []

y = []

def f(x):
    return 3*x+2
for i in range(6):
    x.append(i)
    y.append(f(i))
    
plt.scatter(x,y)
plt.show()