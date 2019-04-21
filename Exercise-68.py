"""Write a Python program to convert pressure in kilo-pascals to pounds per square inch,
a millimeter of mercury (mmHg) and atmosphere pressure."""


def convertor(kps):
	"""return conversion value."""
	print(f"Pressure in kilo pascals: {kps} kilo-pascals")
	psi = str(kps / 6.89475729) + ' psi'
	mmhg = str((kps * 760) / 101.325) + ' mmhg'
	atm = str(kps / 101.325) + ' atm'
	return psi, mmhg, atm


print(f'*****************************************************')
print(f"Pressure in terms of psi, mmhg and atm: {convertor(12.35)}")
print(f'*****************************************************')
