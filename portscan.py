# Ferramenta criada durante o treinamento de Introdução ao Hacking e Pentest da Solyd.
# Site target: bancocn.com
# Porta target: 80

import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('bancocn.com', 80))
cliente.send('hauhsas\n\n')
resposta = cliente.recv(1024)

print resposta







