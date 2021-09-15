import InsectClass as i


mosquito = i.Insect(2, 4)
housefly = i.Insect(2, 4)


mosquito.flight_length()

housefly.flight_length()

print("the mosquito can fly up to", mosquito.get_miles(), "miles")
print("the housefly can fly up to", housefly.get_miles(), "miles")
