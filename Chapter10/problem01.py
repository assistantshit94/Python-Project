class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Shital", 1200000, 561004)
print(p.name, p.salary, p.pin)
r = Programmer("Rinu", 1200000, 610000)
print(r.name, r.salary, r.pin)
