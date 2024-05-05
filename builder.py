# House Product
class House:
    def __init__(self, foundation, walls, roof, doors, windows):
        self.foundation = foundation
        self.walls = walls
        self.roof = roof
        self.doors = doors
        self.windows = windows

    def display(self):
        print("House with:")
        print(f"Foundation: {self.foundation}")
        print(f"Walls: {self.walls}")
        print(f"Roof: {self.roof}")
        print(f"Doors: {self.doors}")
        print(f"Windows: {self.windows}")

# House Builder
class HouseBuilder:
    def __init__(self):
        self.foundation = None
        self.walls = None
        self.roof = None
        self.doors = None
        self.windows = None

    def build_foundation(self, foundation):
        self.foundation = foundation
        return self

    def build_walls(self, walls):
        self.walls = walls
        return self

    def build_roof(self, roof):
        self.roof = roof
        return self

    def build_doors(self, doors):
        self.doors = doors
        return self

    def build_windows(self, windows):
        self.windows = windows
        return self

    def build(self):
        return House(self.foundation, self.walls, self.roof, self.doors, self.windows)

# Director
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_simple_house(self):
        return self.builder \
            .build_foundation("Simple Foundation") \
            .build_walls("Simple Walls") \
            .build_roof("Simple Roof") \
            .build_doors("Simple Doors") \
            .build_windows("Simple Windows") \
            .build()

    def construct_luxury_house(self):
        return self.builder \
            .build_foundation("Luxury Foundation") \
            .build_walls("Luxury Walls") \
            .build_roof("Luxury Roof") \
            .build_doors("Luxury Doors") \
            .build_windows("Luxury Windows") \
            .build()

# Client code
if __name__ == "__main__":
    builder = HouseBuilder()
    director = Director(builder)

    simple_house = director.construct_simple_house()
    luxury_house = director.construct_luxury_house()

    simple_house.display()
    print("\n")
    luxury_house.display()
