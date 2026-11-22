import alchemy

print(alchemy.create_air())
try:
	print(alchemy.create_earth())
except Exception as e:
	print('create_earth is not exposed')