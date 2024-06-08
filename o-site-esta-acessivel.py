#import urllib
#import urllib.request

#try:
#    site = urllib.request.urlopen('https://www.peritoanimal.com.br/')
#except urllib.error.URLError:
#    print('O site pudim não está acessível no momento')
#else:
#   print('Consegui acessar o site Pudim com sucesso.')
#   print(site.read())


import urllib
import urllib.request

try:
    site = input('Insira o link do site: ')
    check = urllib.request.urlopen(site)
    print('Site está acessível.')
except:
    print(f'Site está indisponível.')


#class Cachorro:
#    def __init__(self, nome, idade):
#        self.nome = nome
#        self.idade = idade
#    
#    def latir(self):
#        print(f"{self.nome} está latindo!")
#        
# Criando um objeto da classe Cachorro
#meu_cachorro = Cachorro("Rex", 3)

# Acessando atributos e chamando métodos do objeto
#print(f"O nome do cachorro é {meu_cachorro.nome} e ele tem {meu_cachorro.idade} anos.")
#meu_cachorro.latir()
