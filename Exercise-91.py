"""Write a Python program to create a copy of its own source code."""
a = ['print("a =", a)', 'for s in a: print s']
print("a =", a)
for s in a: print(s)
