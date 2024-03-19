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

def bezier(control_points, iterations):
    if iterations == 0:
        return np.array([control_points[0], control_points[2]])
    
    mid1 = midpoint(control_points[0] ,control_points[1]) 
    mid2 = midpoint(control_points[1] ,control_points[2]) 

    mid12 = midpoint(mid1, mid2) 

    left = [control_points[0], mid1, mid12,]
    right = [mid12, mid2, control_points[2]]
    leftmid = bezier(left, iterations - 1)
    rightmid = bezier(right, iterations - 1)

    return np.concatenate([leftmid[:-1], rightmid])

control_points = []
for i in range (3):
    print(f"\nKordinat titik kontrol ke {i+1}")
    x = int(input("Masukkan absis (x): "))
    y = int(input("Masukkan ordinat (y): "))
    control_points.append([x,y])

iterations = int(input("Masukkan jumlah iterasi: "))

cp = np.array(control_points)
start = time.time()
points = bezier(control_points, iterations)
end = time.time()
runtime = end - start
print("Runtime", runtime, "seconds")

# print(len(points))

plot_curve(points, cp,f"Divide and Conquer Bezier Curve : {runtime} seconds")
