import base64
import sys

args = sys.argv
print args[1]
enco = base64.b64encode(args[1])
print enco
for num in range(16):
    decd = base64.b64decode(enco)
    enco = decd

print decd
