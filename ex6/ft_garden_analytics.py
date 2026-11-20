class Plant:

    class PlantStats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def record_grow(self) -> None:
            self._grow_count += 1

        def record_age(self) -> None:
            self._age_count += 1

        def record_show(self) -> None:
            self._show_count += 1

    def __init__(self, p_name: str, p_height: int, p_age: int) -> None:
        self._name = p_name
        if p_height < 0:
            self._height = 0
        else:
            self._height = p_height
        if p_age < 0:
            self._age = 0
        else:
            self._age = p_age
        self._stats = self.PlantStats()

    # staticmethod
    @staticmethod
    def check_age(age: int) -> bool:
        if age > 365:
            return True
        return False
    
    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"{self._name.capitalize()}: Error, height can’t ", end="")
            print("be negative")
            print("Height update rejected")
            return
        self._height = new_height
        print(f"Height updated:  {self._height:.0f}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name.capitalize()}: Error, age can’t be negative")
            print("Age update rejected")
            return
        self._age = new_age
        print(f"Age updated:  {self._age}days")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self._name.capitalize()}: {self.get_height():.1f}cm,", end="")
        print(f" {self.get_age()} days old")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_bloom = False

    def bloom(self) -> None:
        self.is_bloom = True

    def grow(self, growth_rate: float) -> None:
        self._stats.record_grow()
        self._height += growth_rate

    def age(self) -> None:
        self._stats.record_age()
        self._age += 1

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.is_bloom:
            print(f"{self._name.capitalize()} is blooming beautifully!")
        else:
            print(f"{self._name.capitalize()} has not bloomed yet")

class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk
        self._shade_count = 0

    def produce_shade(self) -> None:
        self._shade_count += 1
        print(f"Tree {self._name.capitalize()} now produces ", end="")
        print(f"a shade of {self._height:.1f}cm ", end="")
        print(f"long and {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}")

class Seed(Flower):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seed = 0

    def bloom(self) -> None:
        super().bloom()
        self.seed += 4
    
    def grow_and_age(self, growth_rate: float, days: int) -> None:
        for i in range(days):
            self.grow(growth_rate)
            self.age()
            self.bloom()

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seed}")




def display_plant_stats(plant: Plant) -> None:
    print("Stats: ", end="")
    print(f"{plant._stats._grow_count} grow, ", end="")
    print(f"{plant._stats._age_count} age, ", end="")
    print(f"{plant._stats._show_count} show")

if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")
    p_one = Flower("rose", 15, 10, "red")
    p_two = Tree("oak", 200, 265, 5)
    p_three = Seed("sunflower", 80, 45, "yellow") 
    anonymous = Plant.anonymous_plant()
    print()
    print("=== Flower")
    p_one.show()
    print(f"[statistics for {p_one._name.capitalize()}]")
    display_plant_stats(p_one)
    print(f"[asking the {p_one._name} to grow and bloom]")
    p_one.grow(0.5)
    p_one.bloom()
    p_one.show()
    print(f"[statistics for {p_one._name.capitalize()}]")
    display_plant_stats(p_one)
    print()
    print("=== Tree")
    p_two.show()
    print(f"[statistics for {p_two._name}]")
    display_plant_stats(p_two)
    print(f"{p_two._shade_count} shade")
    print(f"[asking the {p_two._name} to produce shade]")
    p_two.produce_shade()
    print(f"[statistics for {p_two._name}]")
    display_plant_stats(p_two)
    print(f"{p_two._shade_count} shade")
    print()
    print("=== Seed")
    p_three.show()
    print("[make sunflower grow, age and bloom]")
    p_three.grow_and_age(0.5, 15)
    p_three.show()
    print(f"[statistics for {p_three._name.capitalize()}]")
    display_plant_stats(p_three)
    print()
    print("=== Anonymous")
    anonymous.show()
    display_plant_stats(anonymous)


