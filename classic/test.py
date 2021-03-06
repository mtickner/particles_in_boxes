from particle import Particle
import matplotlib.pyplot as plt
r = 1
p = Particle(500, [0, 0], [0.0, 0.0], [0, 0], resolution = r, prev_vel = [0.0, 0.0])
q = Particle(500, [5, 0], [0, 0.0], [0, 0], prev_pos = [5, 0], resolution = r, prev_vel = [0, 0.0])

result = "Distance: {}\n Unit Vector: {}\n Force Vector: {}\n Position: {}\n"
dist = [q.calcDistance(p)]
vel = [q.calcV()]

nq = q.next(p)
np = p.next(q)
dist.append(nq.calcDistance(p))
vel.append(nq.calcV())
t = [0, 1]
for i in range(2, 250):
    nq = nq.next(np)
    np = np.next(nq)
    dist.append(nq.calcDistance(np))
    vel.append(nq.calcV())
    t.append(i*r)

vx = [x[0] for x in vel]
vy = [y[1] for y in vel]
plt.plot(t, vx)
plt.plot(t, vy)
plt.show()
