fogy:float = float(input('gépkocsi fogyasztása 100 Km-en (l): '))
ar:int = int(input('benzin literenkénti ára (HUF): '))
ut:float = float(input('megtett út hossza (Km): '))

koltseg:float = round(fogy * ar * ut / 100)

print(f'útiköltség: {koltseg} HUF')