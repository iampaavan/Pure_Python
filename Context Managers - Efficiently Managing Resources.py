class Open_File():
	
	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
		
	def __enter__(self):
		self.file = open(self.filename, self.mode)
		return self.file
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.file.close()
	
	
with Open_File('sample.txt', 'w') as f:
	f.write('Context Manager - Implemented using Class. ')
	
print(f.closed)
