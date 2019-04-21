import struct
"""Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS?"""

print(f"Python shell is operating in: {struct.calcsize('P') * 8} bit mode.")
