class Cocomo:
    def __init__(self, a: float, b: float, c: float, d: float):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def effort(self, kloc: float) -> float:
        """Calculate the effort in person-months."""
        return self.a * (kloc ** self.b)
    
    def time(self, kloc: float) -> float:
        """Calculate the development time in months."""
        effort = self.effort(kloc)
        return self.c * (effort ** self.d)

class OrganicCocomo(Cocomo):
    def __init__(self,a=2.4, b=1.05, c=2.5, d=0.38):
        super().__init__(a,b,c,d)
        self.cost_driver =0


class SemiDetachedCocomo(Cocomo):
    def __init__(self,a=3,b=1.12,c=2.5,d=0.35):
        super().__init__(a,b,c,d)
        self.cost_driver = 1

    def set_cost_driver(self, cost_driver: float):
        self.cost_driver = cost_driver

    def effort(self, kloc: float) -> float:
        base_effort = super().effort(kloc)
        return base_effort * self.cost_driver
    
    def time(self, kloc: float) -> float:
        effort = self.effort(kloc)
        return self.c * (effort ** self.d)

class EmbeddedCocomo(Cocomo):
    def __init__(self,a=3.6, b=1.20, c=2.5, d=0.32):
        super().__init__(a,b,c,d)
        self.cost_drivers={}

    def set_cost_drivers(self, cost_drivera: dict):
        self.cost_drivers = cost_drivera

    def cost_driver_multiplier(self) -> float:
        multiplier = 1.0
        for driver, value in self.cost_drivers.items():
            multiplier *= value
        return multiplier

    def effort(self, kloc: float) -> float:
        base_effort = super().effort(kloc)
        return base_effort * self.cost_driver_multiplier()
    
    def time(self, kloc: float) -> float:
        effort = self.effort(kloc)
        return self.c * (effort ** self.d)
    
