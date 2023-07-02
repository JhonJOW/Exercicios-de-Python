from emoji import emojize
from time import sleep
for fogos in range(10, 3, -1):
    print(fogos, '!')
    sleep(1)
for fogos in range(3, 0, -1):
    print(fogos, '!!!')
    sleep(1)
for fogos in range(0, 3):
    print(emojize(':party_popper::partying_face::party_popper:'))
    print(emojize(':partying_face::party_popper::partying_face:'))