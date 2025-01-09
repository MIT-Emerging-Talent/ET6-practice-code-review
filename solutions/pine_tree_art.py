def draw_tree():
    tree = []
    height = 10
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        tree.append(spaces + stars + spaces)
    
    trunk_width = 3
    trunk_height = 3
    trunk = ' ' * (height - 2) + '|' * trunk_width
    
    for _ in range(trunk_height):
        tree.append(trunk)
    
    return '\n'.join(tree)

print(draw_tree())