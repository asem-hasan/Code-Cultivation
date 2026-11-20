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
    print("=== Garden Plant Growth ===")
    p_one.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        p_one.grow(0.8)
        p_one.age()
        p_one.show()
    print(f"Growth this week: {p_one.f_height - p_one.i_height:.1f}cm")
