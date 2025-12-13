# prompt the user for the mass in kg as an integer
# multiply it by the speed of light raised to the power of 2 speed of light = c = 300000000
# Then print Energy (E) in joules

m = int(input("Input the mass in Kg: "));
c = 300000000;

e = m * (c**2);

print("E:", e);
