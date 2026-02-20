from threedfigures import cone_curved_surface_area,cone_volume,cone_total_surface_area
r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Curved Surface Area:", cone_curved_surface_area(r, h))
print("Total Surface Area:", cone_total_surface_area(r, h))
print("Volume:", cone_volume(r, h))