from operator import itemgetter


class constructeur:
    def __init__(self, disc=None, **values):
        self.values = values
        if type(disc) is dict:
            self.values = dict(disc)
        else:
            pass

    def __repr__(self):
        return f"{self.values}"

    def get(self, key, default=None):
        return self.values[key]

    def keys(self):
        return self.values.keys()

    def values_d(self):
        return self.values.values()

    def items(self):
        return self.values.items()

    def sort(self):
        sort1 = sorted(self.values.items(), key=lambda x: x[1])
        self.values = dict(sort1)
        return self.values

    def reverse(self):
        sort1 = sorted(self.values.items(), key=lambda x: x[1], reverse=True)
        self.values = dict(sort1)
        return self.values

    def __getitem__(self, item):
        return self.values[item]

    def __setitem__(self, key, value):
        self.values[key] = value
        return self.values

    def __add__(self, other):
        try:
            other = dict(other)
            self.values.update(other)
            return self.values
        except TypeError:
            print(f"La veleur {other} c'est une variable {type(other)} on perme que dict")
    def test_add(self):
        print(self.values.keys())

    def __delitem__(self, key):
        del self.values[key]
        return self.values

    def __iter__(self):
        for item in self.values.keys():
            yield item

    def __contains__(self, item):
        return item in self.values

    def __len__(self):
        return len(self.values)


# Test d'exemple de manipulation

fruit = constructeur()
print(fruit)
fruit["pommes"] = 52
fruit["poire"] = 34
fruit["prune"] = 128
fruit["melon"] = 15
print(fruit)
fruit.sort()
print(fruit)
legumes = constructeur(carrote=26, haricot=48)
print(legumes)
print(len(legumes))
legumes.reverse()
fruit = fruit + legumes
print(fruit)
del fruit['haricot']
print('haricot' in fruit)
print(legumes['haricot'])
for cle in legumes:
    print(cle)

print(legumes.keys())
print(legumes.values_d())
for nom, qtt in legumes.items():
    print(f"{nom} ({qtt})")
# test = constructeur()
#
# print(test)
# disct = {1: "hola", 2: "ejemplo", 3: "test"}
# print(type(disct))
# test2 = constructeur(disct)
# print(test2)
# test3 = constructeur(cle1="je suis", cle2="andres")
# print(test3.get("cle1", 0))
# print("Separateur--------")
# test4 = test3["cle2"]
# print(test4, "\n")


# test5 = constructeur()
# print(test5)
# test5["pomme"] = 52
# test5["poire"] = 34
# test5["prune"] = 128
# test5["melon"] = 15
# print(test5, "\n")
# for element in test5:
#     print(element)

# del test5["pomme"]
# print(test5)

# print("poire" in test5)
# print(len(test5))
# test5.sort()
# print(test5)

# test6 = sorted(test5.items(), key=lambda x: x[1])
# print(test6)
# test6 = dict(test6)
# print(test6)
# test6_2 = [element.split(',') for element in test6]
# test6_3 = dict((key, value) for key, value in test6_2)
# print(test6_3)
