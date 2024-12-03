import win32api
import win32con
import pyautogui as pag
import keyboard
from time import sleep

# Bot que zera o jogo:
# https://gameforge.com/en-US/littlegames/magic-piano-tiles/
# Para utilizar o bot deve-se entrar no link acima, e rodar o codigo na com a tela de START à direita.

def click(pos):
    win32api.SetCursorPos(pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def localizarCentroImagem(path, conf=1, alert=False):
    for i in range(5):
        try:
            pos = pag.locateCenterOnScreen(path, confidence=conf)
        except pag.ImageNotFoundException as error:
            if alert == True:
                pag.alert(text='Não foi possível localizar a imagem', title='Erro', button='Ok')  
            conf -= 0.1
    return pos

path = '.\\img\\start_button.png'

box_1_center = (925, 328)
box_2_center = (991, 328)
box_3_center = (1057, 328)
box_4_center = (1123, 328)
box_color = (0, 0, 0)
delay = 0.5

pos = localizarCentroImagem(path)
start_button = (int(pos.x), int(pos.y))
pag.click(start_button, duration=delay)

while keyboard.is_pressed('1') == False:
    if pag.pixelMatchesColor(box_1_center[0], box_1_center[1], box_color):
        click(box_1_center) 
    if pag.pixelMatchesColor(box_2_center[0], box_2_center[1], box_color):
        click(box_2_center)
    if pag.pixelMatchesColor(box_3_center[0], box_3_center[1], box_color):
        click(box_3_center)
    if pag.pixelMatchesColor(box_4_center[0], box_4_center[1], box_color):
        click(box_4_center)
