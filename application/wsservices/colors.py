__author__ = 'Dani Meana'

colors = ["#e91e64", "#2196f3", "#ff5722", "#4caf50", "#673ab7", "#ffeb3b"]


def next_color():
    color = colors.pop(0)
    colors.append(color)
    return color