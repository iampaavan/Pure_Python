import os
"""Write a Python program to get the effective group id, effective user id, real group id,
a list of supplemental group ids associated with the current process."""

"""Available only in Linux"""


def process_details():
	"""return process details."""
	effective_group = os.getegid()
	effective_user_id = os.geteuid()
	real_group_id = os.getgid()
	list_supplemental_group_id = os.getgroups()
	return effective_group, effective_user_id, real_group_id, list_supplemental_group_id


print(f'******************************************')
print(f"Effective Group ID: {process_details()[0]}")
print(f'******************************************')
print(f"Effective User ID: {process_details()[1]}")
print(f'******************************************')
print(f"Real Group ID: {process_details()[2]}")
print(f'******************************************')
print(f"Supplemental Group ID: {process_details()[3]}")
print(f'******************************************')

