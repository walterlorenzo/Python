from pynput import keyboard

def on_press(key):
    try:
        print(f'Tecla pressionada: {key.char}')  # Se for uma tecla de caractere imprimimos o caractere
    except AttributeError:
        print(f'Tecla especial pressionada: {key}')  # Caso contrário, imprimimos o nome da tecla especial

def on_release(key):
    if key == keyboard.Key.esc:  # Se pressionar a tecla Esc, encerramos o listener
        return False

# Iniciamos o listener para eventos de pressionamento e soltura de teclas
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
