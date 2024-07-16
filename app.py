import pyautogui
from time import sleep

# 1 - clicar em digitar meu usuário (x=686, y=382)
pyautogui.click(x=794, y=383, duration=1)
pyautogui.write('wesley')

# 2 - clicar em digitar minha senha (x=723, y=411)
pyautogui.click(x=723, y=411, duration=1)
pyautogui.write('1234')

# 3 - clicar em "entrar" (x=594, y=431)
pyautogui.click(x=594, y=431, duration=1)

# 4 - extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto, quantidade, preco = linha.strip().split(',')

        # 1 - clicar e digitar produto (x=470, y=373)
        pyautogui.click(x=470, y=373, duration=0.5)
        pyautogui.write(produto)

        # 2 - clicar e digitar quantidade (x=442, y=404)
        pyautogui.click(x=442, y=404, duration=0.5)
        pyautogui.write(quantidade)

        # 3 - clicar e digitar preço (x=442, y=428)
        pyautogui.click(x=442, y=428)
        pyautogui.write(preco)

        # 4 - clicar em registrar (x=306, y=582)
        pyautogui.click(x=306, y=582, duration=0.5)
        sleep(1)
