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
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Oak", 200, 350)
    p3 = Plant("Cactus", 45, 60)
    p4 = Plant("Sunflower", 75, 40)
    p5 = Plant("Fern", 15, 130)
    print("=== Plant Factory Output ===")
    plants = [p1, p2, p3, p4, p5]

    for i in range(5):
        print("Created: ", end="")
        plants[i].show()
