import os, platform
"""Write a Python program to get OS name, platform and release information."""

print(f'**************************************************')
print(f"OS Information: {os.name}")
print(f'**************************************************')
print(f'OS CPU information: {os.cpu_count()}')
print(f'**************************************************')
print(f"Platform system information: {platform.system()}")
print(f'**************************************************')
print(f'Platform release information: {platform.release()}')
print(f'**************************************************')
print(f'Platform version information: {platform.version()}')
print(f'**************************************************')
