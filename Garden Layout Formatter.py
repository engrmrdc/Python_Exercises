# Create a function named gardenLayoutFormatter that receives flowerDescriptions and order as its parameters.
# This function aims to format and sort a list of flower descriptions based on a specified ordering criteria.
# 
# The function should perform the following steps:
# 1. Format and sort the concatenated list based on the order parameter:
# 2. If order is 'name', sort the flowers alphabetically by name and format each flower as "The {name} flower is {color} and grows up to {height} cm tall."
# 3. If order is 'color', sort the flowers alphabetically by color and format each flower as "A {color} flower named {name}, with a height of {height} cm."
# 4. If order is 'height', sort the flowers by their height (from shortest to tallest) and format each flower as "{height} cm: the {color} {name} reaches this height."
# 5. Return the formatted and sorted flower descriptions as a single string, with each description on a new line.
#
# Parameters
# flowerDescriptions (list of str): A list of strings where each string represents a description of a flower in the format "name:color:height". For example, ["Rose:red:50", "Lily:white:80", "Tulip:yellow:30"].
# order (str): A string that specifies the ordering of the flowers based on their attributes. It can be one of the following values: 'name', 'color', or 'height'.
# The function returns a string containing the formatted and sorted flower descriptions, with each description on a new line.


def gardenLayoutFormatter(flowerDescriptions, order):
    if order == 'name':
        flowerDescriptions.sort()
        for i in flowerDescriptions:
            a = i.split(":")
            print(f'The {a[0]} flower is {a[1]} and grows up to {a[2]} cm tall.')
            print(f'The {a[0]} flower is {a[1]} and grows up to {a[2]} cm tall.')
    elif order == 'color':
        order_lst = []
        for i in flowerDescriptions:
            a = i.split(":")
            order_lst.append(a)
            order_lst.sort(key = lambda x: x[1])
        for i in order_lst:
            print(f'A {i[1]} flower named {i[0]}, with a height of {i[2]} cm.')
            print(f'A {i[1]} flower named {i[0]}, with a height of {i[2]} cm.')
    elif order == 'height':
        order_lst = []
        for i in flowerDescriptions:
            a = i.split(":")
            order_lst.append(a)
            for i in order_lst:
                i[2] = int(i[2])
        order_lst.sort(key=lambda x: x[2])
        for i in order_lst:
            print(f'{i[2]} cm: the {i[1]} {i[0]} reaches this height.')
            print(f'{i[2} cm: the {i[1]} {i[0]} reaches this height.')

# Under this line are the data for testing.

# flowerDescriptions = ['Daisy:blue:25', 'Sunflower:yellow:300', 'Orchid:pink:35']
# order = 'name'

# flowerDescriptions = ['Daisy:blue:25', 'Sunflower:yellow:300', 'Orchid:pink:35']
# order = 'color'

# flowerDescriptions = ['Poppy:red:80', 'Daffodil:yellow:30', 'Lilac:purple:120']
# order = 'height'

gardenLayoutFormatter(flowerDescriptions, order)
