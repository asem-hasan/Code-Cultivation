class Plant:
    def __init__(self, p_name: str, p_height: float, p_age: int) -> None:
        self.p_name = p_name
        self.i_height = p_height
        self.f_height = p_height
        self.p_age = p_age

    def grow(self, growth_rate: float) -> None:
        self.f_height += growth_rate

    def age(self) -> None:
        self.p_age += 1

    def show(self) -> None:
        print(f"{self.p_name}: {self.f_height:.1f}cm, {self.p_age} days old")


if __name__ == "__main__":
    p_one = Plant("Rose", 25, 30)
    p_two = Plant("Oak", 200, 350)
    p_three = Plant("Cactus", 45, 60)
    p_four = Plant("Sunflower", 75, 40)
    p_five = Plant("Fern", 15, 130)
    print("=== Plant Factory Output ===")
    plants = [p_one, p_two, p_three, p_four, p_five]

    for i in range(5):
        print("Created: ", end="")
        plants[i].show()
