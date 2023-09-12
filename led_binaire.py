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


print("debut du test")
for elem,binaire in zip(led,input("entre du binaire ")):
    if int(binaire):
        elem.write(1)
sleep(2.0)
out = lambda t : t.write(0) 
# for elem in led:
#     out(elem)
list(map(out,led))
print("fin du test")
carte.exit()