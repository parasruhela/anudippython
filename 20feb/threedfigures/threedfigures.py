import math

# 1️⃣ Curved Surface Area
def cylinder_curved_surface_area(radius, height):
    return 2 * math.pi * radius * height


# 2️⃣ Total Surface Area
def cylinder_total_surface_area(radius, height):
    return 2 * math.pi * radius * height + 2 * math.pi * radius**2


# 3️⃣ Volume
def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

# 1️⃣ Curved Surface Area
def cone_curved_surface_area(radius, height):
    slant_height = math.sqrt(radius**2 + height**2)
    return math.pi * radius * slant_height


# 2️⃣ Total Surface Area
def cone_total_surface_area(radius, height):
    slant_height = math.sqrt(radius**2 + height**2)
    return math.pi * radius * slant_height + math.pi * radius**2


# 3️⃣ Volume
def cone_volume(radius, height):
    return (1/3) * math.pi * radius**2 * height

# 1️⃣ Curved Surface Area of Cuboid
def cuboid_curved_surface_area(length, width, height):
    return 2 * height * (length + width)


# 2️⃣ Total Surface Area of Cuboid
def cuboid_total_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)


# 3️⃣ Volume of Cuboid
def cuboid_volume(length, width, height):
    return length * width * height
