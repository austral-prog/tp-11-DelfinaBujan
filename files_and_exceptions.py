def read_file_to_dict(filename):
	nuevo_dict=dict()
	try: 
		with open(filename,"r") as archivo:
			contenido=archivo.read()
			i=0 
			while i < len(contenido):
				dos_puntos=contenido.find(":",i)
				punto_coma=contenido.find(";",i)
				if dos_puntos==-1 or punto_coma==-1:
					break
				productos=contenido[i:dos_puntos]	
				valor=contenido[dos_puntos + 1 :punto_coma]
				valorbien=float(valor)
				if productos in nuevo_dict:
					nuevo_dict[productos].append(valorbien)
				else:
					nuevo_dict[productos]=[valorbien]
				i=punto_coma + 1
	except FileNotFoundError:
		raise FileNotFoundError("El archivo no existe")
	return nuevo_dict


def process_dict(data):
	for producto in	data:
		total=0
		for monto in data[producto]:
			total=total+monto
		promedio=total/len(data[producto])
		print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")	
    pass
