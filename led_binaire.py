from pyfirmata import Arduino, util
from time import sleep
carte = Arduino("COM7")
aquisition = util.Iterator(carte)
aquisition.start()
bleu = carte.get_pin("d:2:o")
vert = carte.get_pin("d:3:o")
jaune = carte.get_pin("d:4:o")
sleep(1.0)
led = [jaune, vert, bleu ] 
out = lambda t : t.write(0) 
print("debut du test")
for i in range(8):
    mot = bin(i)[2:]
    while len(mot) != 3:
        mot = "0"+mot
    for elem,binaire in zip(led,mot):
        if int(binaire):
            elem.write(1)
    sleep(1.0)
    list(map(out,led))



print("fin du test")
carte.exit()
