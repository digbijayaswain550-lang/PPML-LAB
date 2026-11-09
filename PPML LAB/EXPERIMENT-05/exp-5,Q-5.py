A = {1, 2, 3}
B = {3, 4, 5}

print("Set A:", A)
print("Set B:", B)

print("Union:", A | B)
print("Intersection:", A & B)
print("A - B:", A - B)
print("B - A:", B - A)
print("Symmetric Difference:", A ^ B)
print("A is subset of B:", A.issubset(B))
print("A is superset of B:", A.issuperset(B))
print("A and B are disjoint:", A.isdisjoint(B))
