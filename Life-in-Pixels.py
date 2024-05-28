import string
def string_to_rgb(input_string):
    res = 0
    rgb = []
    lower = input_string.lower()

    if lower.isalpha() is True:
        for i in lower:
            a = string.ascii_lowercase.index(i) + 1
            res += a
        rgb += res, res*2, res*3
        print(rgb)
    else:
        print([0, 0, 0])

# Input and Expected Outputs
# input_string = 'XYZ'
# E0 = [75, 150, 225]

# input_string = 'XYZ'
# E0 = [75, 150, 225]

# input_string = 'hello'
# E0 = [52, 104, 156]

# input_string = '123abc!XYZ'
# E0 = [0, 0, 0]

string_to_rgb(input_string)
