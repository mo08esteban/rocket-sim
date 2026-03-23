import matplotlib.pyplot as plt

# 参数
mdot = 0.8
g = 9.8
thrust = 2000
mass = 100
dt = 0.1
t_max = 10

# 初始化
t = 0
v = 0
h = 0
time_list = []
height_list = []

# 模拟循环
while t <= t_max:
    # 质量减少（燃料消耗）
    mass = mass - mdot * dt
    # 如果质量变成负数，就停止（燃料耗尽）
    if mass <= 0:
        break
    a = thrust / mass - g
    v = v + a * dt
    h = h + v * dt
    time_list.append(t)
    height_list.append(h)
    t = t + dt

plt.plot(time_list, height_list)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Rocket Trajectory")
plt.savefig('trajectory.png')   # 保存为图片
print("轨迹图已保存为 trajectory.png")