# Convert the input number to float
nx = float(input('Enter Original x in Flout Format: '))
ny = float(input('Enter Original y in Flout Format: '))
# We separate the decimal from the number and save the correct part of the number
nxi = int(nx)
nyi = int(ny)
nxs = str(nx-nxi)
nys = str(ny-nyi)
enx = str(nxi**2-7)
eny = str(nyi**3-6)
print('Encrypted x is :'+' '+enx+'.'+nxs)
print('Encrypted y is :'+' '+eny+'.'+nys)

# Name of the programmer: Maryam Jamali
# Email address: m.jamali16@yahoo.com
# GitHub address: https://github.com/MaryaJamali
