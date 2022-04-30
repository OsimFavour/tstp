class HashTable:
    """Hash table data structure"""
    def __init__(self) -> None:
        self.list = [None] * 11

    @staticmethod
    def hash(n):
        """
        :param n: int
        :return: return index in list to store number:
        """
        return n % 11

    def set(self, n, v):
        """
        param n: int
        param v: can be any type
        """
        self.list[self.hash(n)] = v

    def get(self, n):
        """
        :param n: int
        :return: int value from list
        """
        return self.list[hash(n)]

hash_table = HashTable()
hash_table.set(1, "Disrupted")
hash_table.set(5, "HubSpot")
hash_table.set(10, "Favour is King")
print(hash_table.get(1))
print(hash_table.get(5))
print(hash_table.get(10))