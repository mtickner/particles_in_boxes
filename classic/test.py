from particle import Particle

p = Particle(500, [0, 0], [0, 0], [0, 0])
q = Particle(50, [1, 1], [0, 0], [0, 0])

dist = p.calcDistance(q)
unit = p.unitVector(q)
force = p.calcForce(q)

print(dist, unit, force)
