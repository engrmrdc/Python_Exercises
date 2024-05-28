# Life in Pixels
#
# Computer screens display images by representing each pixel with three color values: red, green, and blue (RGB). Each color is represented by an integer value ranging from 0 to 255.
# 
# Develop a function named string_to_rgb that takes a string and returns a list of three integers representing the red, green, and blue values of the string's RGB color. The function should return [0, 0, 0] if the input string is empty or if it contains any non-alphabetic characters.
# 
# when mapping a string to RGB values:
# 
# 1. Each letter is assigned a numeric value based on its position in the alphabet. (a is 1, b is 2 and so on)
# 2. This numeric value is multiplied by specific factors (1 for red, 2 for green, and 3 for blue).
# 3. The resulting values are accumulated for the red, green, and blue components.
# 4. Ensure each component stays within the range of 0 to 255.
# 5. The final RGB color is returned as a list: [red, green, blue]
#
# ** The mapping is case-insensitive, so both uppercase and lowercase letters are treated the same.

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

# Another solution

def string_to_rgb(input_string):
    # Check if the input string is empty or contains non-alphabetic characters.
    if not input_string.isalpha():
        return [0, 0, 0]

    # Convert the input string to lowercase for case-insensitive mapping.
    input_string = input_string.lower()

    # Initialize RGB values to 0.
    red, green, blue = 0, 0, 0

    # Map each character to RGB values.
    for char in input_string:
        char_value = ord(char) - ord('a') + 1  # Map 'a' to 1, 'b' to 2, and so on.
        red = (red + char_value) % 256
        green = (green + char_value * 2) % 256
        blue = (blue + char_value * 3) % 256

    return [red, green, blue]

# Under this line are the data for testing.

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
