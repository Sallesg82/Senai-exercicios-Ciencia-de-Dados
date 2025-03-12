# Exercício 7

# Considere dois países: 
# A com 80.000 habitantes e taxa de crescimento anual de 3% 
# B com 200.000 habitantes e taxa de 1,5%. 

# Determine quantos anos serão necessários para que a população do país A ultrapasse a população do país B.


popuA = 80000

popuB = 200000

anos = 0 


while popuA <= popuB:
    popuA *= 1.03
    popuB *= 1.015
    
    anos += 1

print(anos)
