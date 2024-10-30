import serial
import time

velocidade = "o5 km"

try:

    conexao = serial.Serial("COM7", 9600, timeout=0.5)
    time.sleep(2)
    print(conexao)
    print("Conecxao na porta", conexao.portstr)
    print(velocidade)
    conexao.write(velocidade.encode(encoding='ascii'))
    conexao.flush()
    time.sleep(2)

except serial.SerialException:
    print("nao conectado")
    pass

# while True:
#     serialstring = ""
#     velocidade = input("Digite o comando ")

#     conexao.write(velocidade.encode(encoding='ascii', errors='strict'))
    

#     break
conexao.close()
print("Conecao fechada")

