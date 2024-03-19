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

def koefisien(n):
    base = [1,1]
    if n==1:
        return base
    else :
        new = []
        for i in range(1, n):
            new = [1 for i in range(len(base)+1)]
            for j in range (1,len(new)-1):
                new[j] = base[j-1]+base[j]
            base = new
        return new

def curve_point(control_points, iterations):
    n = len(control_points)
    curve_points = []
    koef = koefisien(n-1)
    for j in range(2**iterations + 1):
        x=0
        y=0
        t = j / (2**iterations)
        for i in range (n):
            x += koef[i] * (1-t)**(n-1-i) * t**i * control_points[i][0]
            y += koef[i] * (1-t)**(n-1-i) * t**i * control_points[i][1]
        curve_points.append([x, y])
    return np.array(curve_points)


n = int (input("Masukkan banyaknya titik kontrol: "))
control_points = []
for i in range (n):
    print(f"\nKordinat titik kontrol ke {i+1}")
    x = int(input("Masukkan absis (x): "))
    y = int(input("Masukkan ordinat (y): "))
    control_points.append([x,y])

iterations = int(input("\nMasukkan jumlah iterasi: "))

start = time.time()
points = curve_point(control_points, iterations)
end = time.time()
runtime = end - start
print("Runtime", runtime, "seconds")

cp = np.array(control_points)
plot_curve(points,cp,"Brute Force Bezier Curve")
