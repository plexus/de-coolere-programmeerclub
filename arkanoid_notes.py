
# dictionaries
# tuples

bal = {"x": 0,
       "y": 0,
       "grootte": 20,
       "richting": (5,2)}

bal["grootte"]

def beweeg_bal(bal):
    bal["x"]+=bal["richting"][0]
    bal["y"]+=bal["richting"][1]

beweeg_bal(bal)
beweeg_bal(bal)

print("x=" + str(bal["x"]))
print("y=" + str(bal["y"]))
