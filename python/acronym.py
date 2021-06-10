acronym = ['LOL', 'SMH', 'IDK', 'BRB', 'TBH']


print(acronym[1])
print(acronym[len(acronym)-1])
acronym.append("ROFL")
acronym.append('JIYONEE')

print(acronym[len(acronym)-1])

print(acronym[0])

if "BFN" in acronym:
    print("BFN is in the list")
else:
    print("BFN is NOT in in the list")


for acr in acronym:
    print(acr)
