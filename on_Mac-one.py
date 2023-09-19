curso = '0ytho5 7ara 12i'
print(curso)
print( 'from 1 to 11 :_', curso[1:11])   #so 1 is 'y' and 'a' is 11,    here we print from 1 to 11 = ytho5 7ara
print( 'from 7 to end :_', curso[7:])    #here is from 7 to end = 7ara 12i
print( 'from 4 to 11 :_', curso[4:11] ) #& lastly here is from 4 to 11 = o5 7ara
print( 'from 0 to 15 :_', curso[0:15] ) # and here we print from 0 to 15 = 0ytho5 7ara 12i

#like say, curso stays the same but i wanna change it somewhere else... 
change = curso[7:14]
print( 'from 7 to 14 :_', change)   #prints = 7ara 12

#OR!!! 
cambio = curso[7:]  #goes to the end from 7 = para ti    
print( 'OR from 7 to end :_', cambio)   # = 7ara 12i 

#here starts counting from the end -1, -2, -3, -4, -5 = -i, -t, - , -a, -r,     here prints = ytho5 7ara 12
print( 'Imprime with no "p" at the start and no "i" at the end :_', curso[1:-1])    
