import numpy as np 
ans = np.random.randint(1,101)
max1 = 100
min1 = 1
guess = input('請在{}~{}之間猜一數'.format(min1,max1))
guess = int(guess)
while guess != ans:
    if guess > ans and guess < max1:
        max1 = guess    
    if guess < ans and guess > min1:
        min1 = guess
    guess = input('請在{}~{}之間猜一數'.format(min1,max1))
    guess = int(guess)
print('答對了')