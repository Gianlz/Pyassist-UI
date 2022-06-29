import random as rm
import webbrowser as wb
def RainbowSix():
    wb.open_new_tab("steam://rungameid/359550")
def CSGO():
    wb.open_new_tab('steam://rungameid/730')
def Valorant():
    print("Avaible-Soon")
def DB():
    wb.open_new_tab('steam://rungameid/920490')
def Sup():
    lista = ["steam://rungameid/359550", 'steam://rungameid/730','steam://rungameid/920490']
    c = rm.randint(0,2)
    wb.open(lista[c])
