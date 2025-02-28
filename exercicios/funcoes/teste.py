import lib_vogais as lv

'''
    Testes para as funções criadas na biblioteca "lib_vogais".
'''

#funcao um
print(lv.eh_vogal("a")) #TRUE
print(lv.eh_vogal("A")) #TRUE
print(lv.eh_vogal("G")) #FALSE
print(lv.eh_vogal("g")) #FALSE
print(lv.eh_vogal("1")) #FALSE
print(lv.eh_vogal(""))  #FALSE
print(lv.eh_vogal("ç")) #FALSE  

#funcao dois
print(lv.eh_texto_vogal("aei")) #TRUE
print(lv.eh_texto_vogal("AEI")) #TRUE
print(lv.eh_texto_vogal("AeI")) #TRUE
print(lv.eh_texto_vogal("aEi")) #TRUE
print(lv.eh_texto_vogal("AB"))  #FALSE
print(lv.eh_texto_vogal("BA"))  #FALSE
print(lv.eh_texto_vogal("CD"))  #FALSE
print(lv.eh_texto_vogal("12"))  #FALSE
print(lv.eh_texto_vogal(""))    #FALSE
print(lv.eh_texto_vogal("ç~"))  #FALSE
print(lv.eh_texto_vogal("aaaaaaaaab"))  #FALSE
print(lv.eh_texto_vogal("baaaaaaaaa"))  #FALSE

#funcao tres
print(lv.quantidade_vogais("aei")) #3
print(lv.quantidade_vogais("AEI")) #3
print(lv.quantidade_vogais("AeI")) #3
print(lv.quantidade_vogais("aEi")) #3
print(lv.quantidade_vogais("AB"))  #1
print(lv.quantidade_vogais("BA"))  #1
print(lv.quantidade_vogais("CD"))  #0
print(lv.quantidade_vogais("12"))  #0
print(lv.quantidade_vogais(""))    #0
print(lv.quantidade_vogais("ç~"))  #0
print(lv.quantidade_vogais("aaaaaaaaab"))  #9
print(lv.quantidade_vogais("baaaaaaaaa"))  #9

#funcao quatro
print(lv.remove_vogais("aei")) #"Texto ficou/não tem vogal"
print(lv.remove_vogais("AEI")) #"Texto ficou/não tem vogal"
print(lv.remove_vogais("AeI")) #"Texto ficou/não tem vogal"
print(lv.remove_vogais("aEi")) #"Texto ficou/não tem vogal"
print(lv.remove_vogais("AB"))  #"B"
print(lv.remove_vogais("BA"))  #"B"
print(lv.remove_vogais("CD"))  #"CD"
print(lv.remove_vogais("12"))  #"12"
print(lv.remove_vogais(""))    #"Texto ficou/não tem vogal"
print(lv.remove_vogais("ç~"))  #"ç~"
print(lv.remove_vogais("aaaaaaaaab"))  #"b"
print(lv.remove_vogais("baaaaaaaaa"))  #"b"

#funcao cinco
print(lv.identifica_vogais("aei")) #[aei]
print(lv.identifica_vogais("AEI")) #[AEI]
print(lv.identifica_vogais("AeI")) #[AeI]
print(lv.identifica_vogais("aEi")) #[aEi]
print(lv.identifica_vogais("AB"))  #[A]
print(lv.identifica_vogais("BA"))  #[A]
print(lv.identifica_vogais("CD"))  #[]
print(lv.identifica_vogais("12"))  #[]
print(lv.identifica_vogais(""))    #[]
print(lv.identifica_vogais("ç~"))  #[]
print(lv.identifica_vogais("aaaaaaaaab"))  #[aaaaaaaaa]
print(lv.identifica_vogais("baaaaaaaaa"))  #[aaaaaaaaa]

# funncao seis
print(lv.frequencia_vogais("aei")) #[1,1,1,0,0]
print(lv.frequencia_vogais("AEI")) #[1,1,1,0,0]
print(lv.frequencia_vogais("AeI")) #[1,1,1,0,0]
print(lv.frequencia_vogais("aEi")) #[1,1,1,0,0]
print(lv.frequencia_vogais("AB"))  #[1,0,0,0,0]
print(lv.frequencia_vogais("BA"))  #[1,0,0,0,0]
print(lv.frequencia_vogais("CD"))  #[]
print(lv.frequencia_vogais("12"))  #[]
print(lv.frequencia_vogais(""))    #[]
print(lv.frequencia_vogais("ç~"))  #[]
print(lv.frequencia_vogais("aaaaaaaaab")) #[9,0,0,0,0]
print(lv.frequencia_vogais("baaaaaaaaa"))  #[9,0,0,0,0]

#funcao sete
print(lv.substitui_vogais("aei")) #"***"
print(lv.substitui_vogais("AEI")) #"***"
print(lv.substitui_vogais("AeI")) #"***"
print(lv.substitui_vogais("aEi")) #"***"
print(lv.substitui_vogais("AB"))  #"*B"
print(lv.substitui_vogais("BA"))  #"B*"
print(lv.substitui_vogais("CD"))  #"CD"
print(lv.substitui_vogais("12"))  #"12"
print(lv.substitui_vogais(""))    #""
print(lv.substitui_vogais("ç~"))  #"ç~"
print(lv.substitui_vogais("aaaaaaaaab"))  #"*********b"
print(lv.substitui_vogais("baaaaaaaaa"))  #"b**********"

#funcao oito
print(lv.vogal_mais_frequente("aaei")) #[a]
print(lv.vogal_mais_frequente("AAEI")) #[a]
print(lv.vogal_mais_frequente("AaeeI")) #[ae]
print(lv.vogal_mais_frequente("aEEi")) #[e]
print(lv.vogal_mais_frequente("AB"))  #[a]
print(lv.vogal_mais_frequente("BA"))  #[a]
print(lv.vogal_mais_frequente("CD"))  #[]
print(lv.vogal_mais_frequente("12"))  #[]
print(lv.vogal_mais_frequente(""))    #[]
print(lv.vogal_mais_frequente("ç~"))  #[]
print(lv.vogal_mais_frequente("aaaaaaaaab"))  #[a]
print(lv.vogal_mais_frequente("baaaaaaaaa"))  #[a]

#funcao nove
print(lv.sortear_vogal("aaei")) 
print(lv.sortear_vogal("AAEI")) 
print(lv.sortear_vogal("AaeeI")) 
print(lv.sortear_vogal("aEEi")) 
print(lv.sortear_vogal("AB"))  
print(lv.sortear_vogal("BA"))  
print(lv.sortear_vogal("CD"))  
print(lv.sortear_vogal("12"))  
print(lv.sortear_vogal(""))    
print(lv.sortear_vogal("ç~"))  
print(lv.sortear_vogal("aaaaaaaaab"))  
print(lv.sortear_vogal("baaaaaaaaa"))  