import os

file_path = './Computa-o_Gr-fica/img_com_ruido.jpeg'
if os.path.exists(file_path):
    print("O arquivo foi encontrado.")
else:
    print("O arquivo não foi encontrado. Verifique o caminho.")
