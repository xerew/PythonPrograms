import numpy as np

c = int(input("Enter the columns of the matrix: ")) #eisagwgi stilwn apo ton xristi
r = (input("Enter the rows of the matrix: ")) #eisagwgi seirwn apo ton xristi
bombs = int(input("Enter the number of the bombs: ")) #eisagwgi arithmo vomvwn apo ton xristi

bomb_value = -1 #orizoume to value pou tha exei ston pinaka ( -1 )

matrix = np.zeros(r * c) #dimiourgoume ton pinaka me midenika
matrix[:bombs] = bomb_value
np.random.shuffle(matrix) #kanoume randomize tis vomves ston pinaka
print matrix.reshape(r, c) #print ton kainourgio pinaka