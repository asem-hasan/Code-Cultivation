class Plant:
    def __init__(self, p_name: str, p_height: int, p_age: int) -> None:
        self.name = p_name
        self.height = p_height
        self.age = p_age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    p3 = Plant("Cactus", 30, 120)
    print("=== Garden Plant Registry ===")
    p1.show()
    p2.show()
    p3.show()
