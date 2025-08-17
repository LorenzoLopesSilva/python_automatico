import os
from datetime import date, datetime

hoje = date.today()

agora = datetime.now()

with open("dias.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write(f"\n{agora}")

os.system('git add .')
os.system(f'git commit -m {hoje}')
os.system('git push')
