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
