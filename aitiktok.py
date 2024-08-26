import cv2
import pytesseract
from pytesseract import Output
import pyttsx3  # Para respuestas de voz
import pyautogui  # Para captura de pantalla
import numpy as np  # Para la conversión de imagen

# Establece la ruta de Tesseract si no está en PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\AppData\Local\Programs\Tesseract-OCR\tesseract'

# Función para detectar texto en una imagen
def detect_text(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convierte la imagen a escala de grises
    text = pytesseract.image_to_string(gray, output_type=Output.DICT)  # Realiza OCR en la imagen en escala de grises
    return text  # Devuelve el texto detectado

# Función para responder a un comando detectado con una respuesta de voz
def respond_to_command(command):
    engine = pyttsx3.init()  # Inicializa el motor de síntesis de voz
    # Responde según el comando detectado
    if "hello" in command.lower():
        engine.say("Hello! How can I help you today?")
    elif "bye" in command.lower():
        engine.say("Goodbye! Have a great day!")
    else:
        engine.say("I'm sorry, I didn't understand that.")
    engine.runAndWait()  # Ejecuta la respuesta de voz

# Bucle principal para capturar y procesar la pantalla en tiempo real
while True:
    # Captura la pantalla completa
    screenshot = pyautogui.screenshot()
    frame = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convierte la captura de pantalla a un array de NumPy y luego a BGR para OpenCV

    text = detect_text(frame)  # Detecta texto en la captura de pantalla
    if text:  # Si se detecta texto
        print("Detected Text:", text)  # Imprime el texto detectado en la consola
        respond_to_command(text['text'])  # Responde al comando detectado con voz

    cv2.imshow('Live Stream', frame)  # Muestra la captura de pantalla en una ventana

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Si se presiona la tecla 'q', salir del bucle
        break

# Cierra todas las ventanas
cv2.destroyAllWindows()
