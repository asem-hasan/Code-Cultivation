class Plant:
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

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can’t be negative")
            print("Height update rejected")
            return
        self._height = new_height
        print(f"Height updated:  {self._height:.0f}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can’t be negative")
            print("Age update rejected")
            return
        self._age = new_age
        print(f"Age updated:  {self._age}days")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def show(self) -> None:
        print(f"{self._name}: {self.get_height():.1f}cm, ", end="")
        print(f"{self.get_age()} days old")


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    print("=== Garden Security System ===")
    print("Plant created: ", end="")
    p1.show()
    p1.set_height(-1)
    p1.set_age(-19)
    print("Current state: ", end="")
    p1.show()
