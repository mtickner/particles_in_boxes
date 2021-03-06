
class Particle:
    G = 6.67430e-11
    def __init__(self,  mass, pos, velocity, acc, prev_pos = [0, 0],
     prev_vel = [0, 0], prev_acc = [0, 0], resolution = 1):
        self.mass = mass #scalor
        self.pos = pos #vector
        self.velocity = velocity #vector
        self.acc = acc #vector

        self.prev_pos = prev_pos
        self.prev_vel = prev_vel
        self.prev_acc = prev_acc

        self.resolution = resolution

    def momentum(self):
        """calculate the momentum of the particle"""
        return [self.mass*self.velocity[0], self.mass*self.velocity[1]]

    def calcForce(self, other):
        """calculate the gravitation force vector"""
        m1 = self.mass
        m2 = other.mass
        p1 = self.pos
        p2 = other.pos
        r = self.calcDistance(self, other)
        rhat = self.unitVector(self, other)
        FMag = (m1*m2*G)/r**2
        return [FMag*rhat[0], FMag*rhat[1]]

    def calcDistance(self, other):
        """calculate the distance between two objects"""
        return ((self.pos[0] - other.pos[0])**2 + (self.pos[1] - other.pos[1])**2)**0.5

    def unitVector(self, other):
        """calculate unit vector"""
        diff = [self.pos[0] - other.pos[0], self.pos[1] - other.pos[1]]
        mag = calcDistance(self, other)
        return [diff[0]/mag, diff[1]/mag]

    def calcA(self, other):
        """calculate the acceleration for this moment"""
        F = self.calcForce(self, other)
        return [F[0]/self.mass, F[1]/self.mass]

    def calcV(self):
        """calculate velocity for this moment"""
        pv = self.prev_vel
        pa = self.prev_acc
        dv = [pa[0]*self.resolution, pa[1]*self.resolution]

        return [pv[0] + dv[0], pv[1] + dv[1]]

    def calcPos(self):
        """calculate position for this moment"""
        pp = self.prev_pos
        pv = self.prev_vel
        dp = [pv[0]*self.resolution, pv[1]*self.resolution]

        return [pp[0]+dp[0], pp[1]+dp[1]]
