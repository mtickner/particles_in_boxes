from particle import Particle
import matplotlib.pyplot as plt
r = 10
p = Particle(5.972e24, [0, 0], [0, 0], [0, 0], resolution = r)
q = Particle(5.97e24, [54.6e5, 0], [0, 0], [0, 0], prev_pos = [54.6e5, 0], resolution = r)

result = "Distance: {}\n Unit Vector: {}\n Force Vector: {}\n Position: {}\n"
dist = [q.calcDistance(p)]

nq = q.next(p)
np = p.next(q)
dist.append(nq.calcDistance(p))

for i in range(365*1000):
    nq = nq.next(np)
    np = np.next(nq)
    dist.append(nq.calcDistance(np))

print("plot data")
plt.plot(dist)
plt.show()
