#contoh multiple inheritance sawah
class Sawah():
	def tanaman(self):
		print("Tempat untuk menanam padi")
		
class Petani(Sawah):
	def tanaman(self):
		print("Mengolah sawah")

class Pupuk(Sawah):
	def tanaman(self):
		print("Diberikan untuk tanaman padi")

class Irigasi(Sawah):
	def tanaman(self):
		print("Memberikan pengairan bagi sawah")		

class Lahan(Petani,Pupuk):
	pass

class Air(Irigasi,Pupuk):
	pass
	
class Padi(Sawah):
	harga = 400000
	if harga > 500000:
		print("Harga padi naik")
	elif harga < 500000:
		print("Harga padi turun")
	else:
		print("Harga padi stabil")
		
l = Lahan()
l.tanaman()
a = Air()
a.tanaman()