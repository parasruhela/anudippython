from threedfigures import cuboid_curved_surface_area,cuboid_total_surface_area,cuboid_volume
l = float(input("Enter length: "))
w = float(input("Enter width: "))
h = float(input("Enter height: "))

print("Curved Surface Area of Cuboid:", cuboid_curved_surface_area(l, w, h))
print("Total Surface Area of Cuboid:", cuboid_total_surface_area(l, w, h))
print("Volume of Cuboid:", cuboid_volume(l, w, h))