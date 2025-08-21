import serial
import time
from PIL import Image
import io

PORT = "COM3" 
BAUDRATE = 115200
CHUNK_SIZE = 100 

# Abre e converte a imagem para escala de cinza
with Image.open("imagem4.jpg") as img:
    gray_img = img.convert("L") 

    # Salva na memória
    buffer = io.BytesIO()
    gray_img.save(buffer, format="JPEG")
    image_bytes = buffer.getvalue()

# Inicia serial
ser = serial.Serial(PORT, BAUDRATE)
time.sleep(2)

# Envia o tamanho da imagem
image_size = len(image_bytes)
ser.write(f"{image_size}\n".encode())
print(f"Tamanho da imagem enviado: {image_size} bytes")
time.sleep(1)

start = time.time()

# Envia a imagem em pacotes
for i in range(0, image_size, CHUNK_SIZE):
    chunk = image_bytes[i:i+CHUNK_SIZE]
    ser.write(chunk)
    time.sleep(0.05)

end = time.time()
elapsed = end - start

print(f"\nImagem enviada com sucesso em {elapsed:.2f} segundos.")

ser.close()



