def my_function(x):
    return 5 * x
print (my_function(3))
print (my_function(5))
print (my_function(9))

print()
# rumus: sisi x sisi
def luas_persegi (sisi):
    luas = sisi * sisi
    return luas

#rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
luas_persegi(5)
