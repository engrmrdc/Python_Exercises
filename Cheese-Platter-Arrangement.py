# Create a function named arrange_cheese_platter that receives cheeses and arrangement as its parameters.
# This function arranges the given list of cheeses on a platter according to a specific arrangement string.
# The cheeses parameter is a list of strings representing different types of cheeses. The arrangement parameter is a string consisting of 'L' and 'R', indicating whether each cheese should be placed to the left or right of the previously placed cheeses on the platter.

# To arrange the cheeses:
# Create an empty list to represent the cheese platter.
# -Iterate through each character in the arrangement string:
# -If 'L', insert the next cheese at the beginning of the platter list.
# -If 'R', append the next cheese to the end of the platter list.
# -Return the platter list containing the arranged cheeses.

# Parameters:
# cheeses (list): A list of strings representing different types of cheeses.
# arrangement (str): A string consisting of 'L' and 'R', indicating the arrangement of cheeses on the platter.
# The function returns a list of strings representing the cheeses arranged on the platter according to the specified arrangement.

def arrange_cheese_platter(cheeses, arrangement):
    platter = []

    for i in range(len(cheeses)):
        if arrangement[i] == 'L':
            platter.insert(0, cheeses[i])
        else:
            platter.append(cheeses[i])

    print(platter)

# Under this line are the data for testing.

# cheeses = ['Gouda', 'Edam', 'Maasdam', 'Emmental', 'Gruyere']
# arrangement = 'RLRRL'

# cheeses =  ['Brie', 'Camembert', 'Roquefort', 'Bleu d'Auvergne']
# arrangement = 'LRLR'

arrange_cheese_platter(cheeses, arrangement)
