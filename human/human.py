class Human:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __repr__(self):
        return f"This is a human with the name {self._name}"

    def __len__(self):
        return self._height

    def __add__(self, other):
        if isinstance(other, Human):
            return f"{self._name} married {other._name}"
        else:
            raise TypeError("Can't add Human to other instance of different object")
