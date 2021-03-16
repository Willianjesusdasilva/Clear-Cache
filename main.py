import os

list_path = ['C:\Windows\Prefetch','C:\Windows\Temp', os.getenv('temp')]

def clear_data(locate):
	for raiz, diretorios, arquivos in os.walk(locate):
		for arquivo in arquivos:
			try:
				os.remove(os.path.join(raiz, arquivo))
			except:
				print(arquivo + ' Erro')


for i in list_path:
    clear_data(i)

exit()
