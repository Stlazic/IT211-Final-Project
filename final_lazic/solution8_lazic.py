def celsius_to_kelvin(value_celsius):
    value_kelvin = 0.0
    value_kelvin = value_celsius + 273.15
    #wrote cel instead of celsius
    return value_kelvin

def kelvin_to_celsius(value_kelvin):
    value_celsius = 0.0
    value_celsius = value_kelvin - 273.15
    return value_celsius

value_c = 0.0

value_k = 0.0

#value_c = 10.0

#wrote '2' instead of 'to'
print(value_c, 'C is', celsius_to_kelvin(value_c), 'K')

#value_k = 283.15
#These two 'value_x = value'lines are not necessary they change the starting value
#which is fine but i dont think that is the intention right now, if it was then it
#wouldnt set the value =  0 in the function

print(value_k, 'is', kelvin_to_celsius(value_k), 'C')
#Did not include a K in the print function
#doesnt really matter just legibility


#maybe change value_c/k to an input variable to get the temperature from the user
