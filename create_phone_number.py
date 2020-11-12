list1=([1,2,3,4,5,6,7,7,9,0])

def create_phone_number(x):
     return f'({x[0]}{x[1]}{x[2]}) {x[3]}{x[4]}{x[5]}-{x[6]}{x[7]}{x[8]}{x[9]}'
print(create_phone_number(list1))



