
# declarando as variaveis
anyInt = 1
anyFloat = 1.2
anyName = "Biocode"
myQuote = "qualqur coisa pode ser escrira aqui"
print(anyName)
#input a string do usuario
anyName = input("Whats your name:")
myNewVlaue = anyName.capitalize() #coloca o input string primeira letra maiscula
upperVal = anyName.upper() #coloca todas as letras maiusculas
lowerVal = anyName.lower()

myDNA = "aaatTTTGGGcctaAAAA" #sequencia DNA com letras diferentes
#myDNA = myDNA.lower() #pedi para transformar tudo em minuscula
print(myDNA.lower())

myRna = myDNA.replace("t", "u") #troca todos os t por u
print(myRna)

print(myDNA.count("T")) #conta o numero de T
print(myDNA.find("tT")) #encontra a sequencia pretendida
print(myDNA.startswith("aaat")) #procura se seu objeto começa com determinada sequencia
 

