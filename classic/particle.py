Class Particle:

    def __init__(self,  mass, pos, velocity):
        self.mass = mass #scalor
        self.pos = pos #vector
        self.velocity = velocity #vector

    def momentum(self):
        """calculate the momentum of the particle"""
        return [self.mass*self.velocity[0], self.mass*self.velocity[1]]
    
