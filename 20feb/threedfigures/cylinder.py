from threedfigures import cylinder_curved_surface_area,cylinder_total_surface_area,cylinder_volume

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Curved Surface Area:", cylinder_curved_surface_area(r, h))
print("Total Surface Area:", cylinder_total_surface_area(r, h))
print("Volume:", cylinder_volume(r, h))