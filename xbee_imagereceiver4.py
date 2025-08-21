import serial 
import time

PORT = "COM4"  
BAUDRATE = 115200

# Inicia serial
ser = serial.Serial(PORT, BAUDRATE)
time.sleep(2)

print("Aguardando tamanho da imagem...")

# Recebe tamanho a imagem
size_line = ser.readline().decode(errors='ignore').strip()
while not size_line.isdigit():
    print(f"Ignorado valor inválido: {size_line}")
    size_line = ser.readline().decode(errors='ignore').strip()

image_size = int(size_line)
print(f"Tamanho da imagem recebido: {image_size} bytes")

# Recebe os dados da imagem
received_bytes = b''
while len(received_bytes) < image_size:
    chunk = ser.read(image_size - len(received_bytes))
    if chunk:
        received_bytes += chunk
        print(f"Recebido: {len(received_bytes)}/{image_size} bytes")

# Salva a imagem
with open("imagem_recebida3_2008_4.jpg", "wb") as img_file:
    img_file.write(received_bytes)

print(f"Imagem salva com sucesso ({len(received_bytes)} bytes)")
ser.close()