colors = ['red', 'green', 'blue']
sizes = ['S', 'M', 'L']
origins=['Turkey','Russia','Germany','USA']

for color in colors:  # Outer loop
    for size in sizes:  # Inner loop
        for origin in origins:
            print(f"{color} - {size} - {origin}")
