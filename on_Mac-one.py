
# curso = '0ytho5 7ara 12i'
# print(curso)
# print(len(curso))
# print( 'from 1 to 11 :_', curso[1:11])   #so 1 is 'y' and 'a' is 11,    here we print from 1 to 11 = ytho5 7ara
# print( 'from 7 to end :_', curso[7:])    #here is from 7 to end = 7ara 12i
# print( 'from 4 to 11 :_', curso[4:11] ) #& lastly here is from 4 to 11 = o5 7ara
# print( 'from 0 to 15 :_', curso[0:15] ) # and here we print from 0 to 15 = 0ytho5 7ara 12i

#like say, curso stays the same but i wanna change it somewhere else... 
# change = curso[7:14]
# print( 'from 7 to 15 :_', change)   #prints = 7ara 12

#OR!!! 
# cambio = curso[7:]  #goes to the end from 7 = para ti    
# print( 'OR from 7 to end :_', cambio)   # = 7ara 12i 

#here starts counting from the end -1, -2, -3, -4, -5 = -i, -t, - , -a, -r,     here prints = ytho5 7ara 12
# print( 'unFormatted Strings: Imprime with no "p" at the start and no "i" at the end :_' + curso[1:-1])    



#FORMATTED STRINGS, OR F-STRINGS    to avoid having to concat...
#working on same 17 line
# print('Imprime with no "p" at the start and no "i" at the end')
# print( 'Imprime with no "p" at the start and no "i" at the end :_', curso[1:-1])

# print( f'Formatted Strings: Imprime with no "p" at the start and no "i" at the end : {curso[1:-1]}' )

#to solve conflicts in f strings : 
# print( f'-_{curso}_-_{change}_-_{cambio}_-' )  #the space is only for it to look nice but is ok to use with NO SPACE



#len    i think is to check how many chars 
curso = '0ytho5 7ara 12i'
chars = 'characters'
print(curso)
print( f'{curso.title()}_has this ammount of_{chars}:_{len(curso)}      ( using the "len" function )' )

#again, 'or' 
proteina = 'proteina'
Xchars = len(proteina)
print( f'{ proteina.title() }_has:_{ Xchars }_characters     ( using the "len" function )' )

short = f'"while" "{curso}" has {len(curso)} {chars.title()} '     #full f string expression 
print( short )      #prints = "while" "0ytho5 7ara 12i" has 15 Characters 

#replace
version = ( short.replace('while', 'when ').title() )    
print(version)      #prints = "When " "0Ytho5 7Ara 12I" Has 15 Characters       ,the title added caps to every word soit read it as (short.title())

#find 
print( f'7Ara Location Index: {version.find("7Ara")} ' )
print( f'0Ytho5 location index is: {version.find("0Ytho5")} from: " {version} "' )
#find whats NOT there   result : -1     negativo, as the rest gives  their position
print( f'find "z" from: <{version}> : {version.find("z")} position' )

# in 
poe_ = ' "They who daydream are cognizant of many things which escape those who dream only by night." '
print(poe_)
print('dreamnt' in poe_)    #prints = flase 
print('dream' in poe_)      #prints = true 

print ( f'10+3, 10/3, 10-3, 10*3, 10**3', 10+3, 10/3, 10-3, 10*3, 10**3 )
print( f'10%3', 10%3, f' 10 entre 3 = 9 y sobra 1. the modulos of 10%3 is 1, as one is left.' )
print( f' 36%6', 36%6, f'the result is zero as there is nothing left over')
print( f'  if we do 37%6 the result is:', 37%6, f'as there is one left')

x = 10 
#x = x+3  OR!..
x+=3
print( f'x+=3:',x)
x**=3
print( f'x**=3:',x)
x/=3
print( f'x/=3:',x)
x%=3
print( f'x%=3:',x)
x*=3
print( f'x*=3:',x)
x-=3
print( f'x-=3:',x)
x=10 
print( f'x=10:',x)

y= x+3*2
print(f'x+3*2:',y)    #prints = 16 as order of ops, * comes first.  order last -, +, *, /, **, (), first 

z = (y + 4) * 5**2
print( f'z = (y + 4) * 5**2:', z) 
print(f'5**2:',5**2)
print(f'20*25:',20*25)
print( f'(2+3)*10-3:',(2+3)*10-3 )