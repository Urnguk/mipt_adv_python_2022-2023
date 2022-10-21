import pickle
d = {1: [3], "acc": (3, 7)}
with open("pickle_data.bin", mode="wb") as f:
    pickle.dump(d, f)
with open("pickle_data.bin", mode="rb") as f:
    a = pickle.load(f)
print(type(a), a)
