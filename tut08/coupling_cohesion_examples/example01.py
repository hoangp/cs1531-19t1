'''A function with low cohesion '''
def get_number(question):
    return int(input(question))

def add(num_1, num_2):
    sum = num_1 + num_2
    return sum

print ("The sum of the numbers is: %d" % add())
