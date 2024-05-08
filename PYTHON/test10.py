def vol(r):
    
    s= (4/3)*(3.14)*(r**3)
    return s



s = float(input("Enter the radius of the sphere: "))
m = vol(s)
print(f"the volume of the sphere is {m:.3f}")