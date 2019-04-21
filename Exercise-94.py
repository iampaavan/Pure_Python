"""Write a Python program to get the identity of an object."""


def id_object():
	"""return identity of objects."""
	obj = input(f"Enter the object type:")
	obj_address = id(obj)
	return obj_address


print(f"Identity of the object: {id_object()}")
