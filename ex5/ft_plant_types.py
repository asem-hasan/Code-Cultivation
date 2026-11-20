from ex4.ft_garden_security import Plant


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.is_bloom = False

    def bloom(self) -> None:
        self.is_bloom = True

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

    def produce_shade(self) -> None:
        print(f"Tree {self._name.capitalize()} now produces ", end="")
        print(f"a shade of {self._height:.1f}cm ", end="")
        print(f"long and {self.trunk_diameter:.1f}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = season
        self.nutritional_value = 0

    def grow(self, growth_rate: float) -> None:
        self._height += growth_rate

    def age(self) -> None:
        self._age += 1

    def grow_and_age(self, growth_rate: float, days: int) -> None:
        for i in range(days):
            self.grow(growth_rate)
            self.age()
            self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.harvest_season.capitalize()}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    p_one = Flower("rose", 15, 10, "red")
    p_two = Tree("oak", 200, 365, 5)
    p_three = Vegetable("tomato", 5, 10, "april")
    print("=== Flower")
    p_one.show()
    print(f"[asking the {p_one._name} to bloom]")
    p_one.bloom()
    p_one.show()
    print("=== Tree")
    p_two.show()
    print(f"[asking the {p_two._name} to produce shade]")
    p_two.produce_shade()
    print("=== Vegetable")
    p_three.show()
    print(f"[make {p_three._name} grow and age for 20 days]")
    p_three.grow_and_age(0.4, 20)
    p_three.show()
