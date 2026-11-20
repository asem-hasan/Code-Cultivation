class Plant:
    def __init__(self, p_name: str, p_height: int, p_age: int) -> None:
        self.name = p_name
        self.height = p_height
        self.age = p_age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    p_one = Plant("Rose", 25, 30)
    p_two = Plant("Sunflower", 80, 45)
    p_three = Plant("Cactus", 30, 120)
    print("=== Garden Plant Registry ===")
    p_one.show()
    p_two.show()
    p_three.show()
