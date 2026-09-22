class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        if self.size > 0:
            return self.size*"🍪"
        else:
            return f"0 Cookies."

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self.size += n
        else:
            raise ValueError("Out of bound error.")

    def withdraw(self, n):
        if n <= self.size:
            self.size -= n
        else:
            raise ValueError("Not enough cookies")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, cap=12):
        if not isinstance(cap, int) or cap < 0:
            raise ValueError("Invalid capacity")
        self._capacity = cap

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size=0):
        self._size = size


jar = Jar(-2)
jar.deposit(2)
jar.deposit(7)
jar.withdraw(3)
jar.deposit(7)
print(jar)