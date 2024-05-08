class Budget_item:
    def __init__(self, id, date, cat, amount, desc):
        self.id = id
        self.date = date
        self.cat = cat
        self.amount = amount
        self.desc = desc

    def __str__(self):
        return self.id

    def __repr__(self):
        return self.id
