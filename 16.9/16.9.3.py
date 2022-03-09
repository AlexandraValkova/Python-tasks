class Purse:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Клиент: {self.name}. Баланс: {self.balance}."


client1 = Purse("Иван Петров", "50 руб")
print(client1.__str__())