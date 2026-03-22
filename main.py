import matplotlib.pyplot as plt

# 参数
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
    # 计算加速度 a
    a = thrust / mass - g
    # 更新速度 v
    v = v + a * dt
    # 更新高度 h
    h = h + v * dt
    # 记录时间和高度
    time_list.append(t)
    height_list.append(h)
    # 更新时间
    t = t + dt

plt.plot(time_list, height_list)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Rocket Trajectory")
plt.savefig('trajectory.png')   # 保存为图片
print("轨迹图已保存为 trajectory.png")