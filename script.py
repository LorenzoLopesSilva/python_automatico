import os
from datetime import date

hoje = date.today()

os.system('git add .')
os.system(f'git commit -m {hoje}')
os.system('git push')
