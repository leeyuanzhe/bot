import PIL
import pyautogui

download = "imagens/download.png";
presente = "imagens/presente.png";
while True:
    if pyautogui.locateOnScreen(presente) is not None:
        botao = pyautogui.locateOnScreen(presente)
        pyautogui.click(botao)
        variavel = True;
        while variavel == True:
            print("false")
            if pyautogui.locateOnScreen(download,  confidence=0.7) is not None:
                 botao2 = pyautogui.locateOnScreen(download, confidence=0.7);
                 print(botao2)
                 pyautogui.click(botao2)
                 pyautogui.click(150 , 150)
                 variavel = False;
        print("achou")
    else:
        print("falhou")



