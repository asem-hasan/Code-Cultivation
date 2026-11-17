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
    print("=== Garden Plant Growth ===")
    p1.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        p1.grow(0.8)
        p1.age()
        p1.show()
    print(f"Growth this week: {p1.f_height - p1.i_height:.1f}cm")
