magassag:float = float(input('add meg a magasságod (cm): ')) / 100
suly:int = int(input('add meg a súlyodat (Kg): '))

tti = suly / magassag ** 2

osztaly:str = '-'

if tti < 16: osztaly = 'súlyos soványság'
# TODO: befejezni legközelebb!