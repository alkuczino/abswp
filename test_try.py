import time
import sys
import random

choice_list = ['tak','nie','być może','nigdy w życiu','co Ty sobie myślisz'\
    ,'pojebało?']

while True:
    try:
        print(random.choice(choice_list))
        time.sleep(2)
    except KeyboardInterrupt:
        print('NARA')
        sys.exit()