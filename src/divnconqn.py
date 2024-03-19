import numpy as np
import matplotlib.pyplot as plt
import time

def plot_curve(points, control_points, figure_name):
    plt.figure(figure_name)
    plt.plot(points[:, 0], points[:, 1], 'b-')
    plt.plot(points[:, 0], points[:, 1], 'ro')
    plt.plot(control_points[:,0], control_points[:,1], 'go-')
    plt.title(figure_name)
    plt.show()


def midpoint(point1, point2):
    return [(point1[0] + point2[0]) / 2 , (point1[1] + point2[1]) / 2]

def midalgorithm(control_points):
    if (len(control_points)==1):
        return [control_points[0]]

    mid=[]
    for i in range (len(control_points)-1) :
        mid.append(midpoint(control_points[i], control_points[i+1]))

    return [control_points[0]] + midalgorithm(mid) + [control_points[-1]]

def bezier(control_points, iterations):
    if iterations == 0:
        return np.array([control_points[0], control_points[-1]])

    mid = midalgorithm(control_points)
    m = len(mid)
    if m % 2 == 0:
        left = [mid[i] for i in range(m//2)]
        right = [mid[i] for i in range(m//2, m)]
    else:    
        left = [mid[i] for i in range(m//2 + 1)]
        right = [mid[i] for i in range(m//2, m)]

    leftmid = bezier(left, iterations - 1)
    rightmid = bezier(right, iterations - 1)

    return np.concatenate([leftmid[:-1], rightmid])

control_points = []
n = int(input("Masukkan jumlah titik kontrol: "))
for i in range (n):
    print(f"\nKordinat titik kontrol ke {i+1}")
    x = int(input("Masukkan absis (x): "))
    y = int(input("Masukkan ordinat (y): "))
    control_points.append([x,y])

iterations = int(input("\nMasukkan jumlah iterasi: "))

cp = np.array(control_points)
start = time.time()
points = bezier(control_points, iterations)
end = time.time()
runtime = end - start
print("Runtime", runtime, "seconds")
# print(points)



plot_curve(points, cp,"Divide and Conquer Bezier Curve")
