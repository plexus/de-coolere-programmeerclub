def sum_array(nummers):
    # sorteer lijst met nummers
    nummers.sort()
    # verwijder kleinste getal uit lijst
    nummers.remove(min(nummers))
    # verwijder grootste getal uit lijst
    nummers.remove(max(nummers))
    # neem som
    return sum(nummers)

print(sum_array([1,2,1,3,5,4,5]))
print(sum_array([3]))
print(sum_array([]))