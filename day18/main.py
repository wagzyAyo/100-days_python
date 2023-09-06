"""
import colorgram

color_rgb = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_rgb.append(new_color)
"""
color_list = [(202, 164, 109)(238, 240, 245), (150, 75, 49,), (223, 201, 135), (152, 93, 120), (30, 68, 100),
              (107, 127, 153), (107, 127, 153), (174, 94, 97), (176, 192, 209), (18, 86, 90), (81, 148, 129)]
