
class Particle:

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
        self.G = 6.67430e-11

    def momentum(self):
        """calculate the momentum of the particle"""
        return [self.mass*self.velocity[0], self.mass*self.velocity[1]]

    def calcForce(self, otherP):
        """calculate the gravitation force vector"""
        m1 = self.mass
        m2 = otherP.mass
        r = self.calcDistance(otherP)
        rhat = self.unitVector(otherP)
        FMag = (m1*m2*self.G)/r**2
        return [FMag*rhat[0], FMag*rhat[1]]

    def calcDistance(self, otherP):
        """calculate the distance between two objects"""
        return ((self.pos[0] - otherP.pos[0])**2 + (self.pos[1] - otherP.pos[1])**2)**0.5

    def unitVector(self, otherP):
        """calculate unit vector"""
        diff = [otherP.pos[0] - self.pos[0], otherP.pos[1] - self.pos[1]]
        mag = self.calcDistance(otherP)
        return [diff[0]/mag, diff[1]/mag]

    def calcA(self, otherP):
        """calculate the acceleration for this moment"""
        F = self.calcForce(otherP)
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
