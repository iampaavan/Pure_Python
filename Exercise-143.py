import platform, os
"""Write a Python program to find the operating system name, platform and platform release date."""


def display_os_details():
	"""return os and platform details."""
	os_name = os.name
	platform_name = platform.system()
	platform_version = platform.version()
	return os_name, platform_name, platform_version


print(f"OS Name: {display_os_details()[0]}")
print(f'*******************************************')
print(f"Platform Name: {display_os_details()[1]}")
print(f'*******************************************')
print(f"Platform Version: {display_os_details()[2]}")
print(f'*******************************************')
