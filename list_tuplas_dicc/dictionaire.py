mon_dictionaire = {"Alemania": "Berlin", "Francia": "Paris", "Reino Unido": "Londres", "España": "Madrid"}
mon_dictionaire["Italia"] = "Lisboa"
print(mon_dictionaire)
mon_dictionaire["Italia"] = "Roma"
print(mon_dictionaire)
del mon_dictionaire["Italia"]
print(mon_dictionaire)

# Mon tuple
montupla = ("España", "Francia", "Reino Unida", "Alemania")
print(type(montupla))
mondic = {montupla[0]: "Madrid", montupla[1]: "Paris", montupla[2]: "Je me rapelle pas", montupla[3]: "Berlin"}
print(mondic, "\n", len(montupla))
print(mondic.keys(), "\n", mondic.values(), "\n", len(mondic))