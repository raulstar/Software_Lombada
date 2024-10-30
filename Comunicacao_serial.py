import serial
import time


def envia(numero):

    try:

        conexao = serial.Serial("COM7", 9600, timeout=0.5)
        print("Conecxao na porta", conexao.portstr)
        time.sleep(2)
        conexao.write(numero.encode(encoding='ascii', errors='strict'))
        conexao.flush()
        #time.sleep(2)
        conexao.close()
        print("enviado " + numero)

    except serial.SerialException:
        print("nao conectado")
        pass

#numero = "df"
#envia(numero)

