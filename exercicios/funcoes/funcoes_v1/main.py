import exercicios.funcoes.funcoes_v1.lib_vogais as lv

def imprime_tracos():
    print("="*60)

while True:
    imprime_tracos()
    print("1 - Verificar se um texto é formado apenas por vogais.")
    print("2 - Contar a quantidade de vogais em um texto.")
    print("3 - Exibir o texto sem as vogais.")
    print("4 - Exibir o texto substituindo as vogais por * (asterísco).")
    print("5 - Exibir as vogais presentes no texto.")
    print("6 - Exibir a frequência de cada vogal no texto.")
    print("7 - Exibir a(s) vogal(is) que mais aparece(m) no texto.")
    print("8 - Sortear uma vogal aleatória no texto.")
    print("9 - Sair.")
    imprime_tracos()
    
    print("Qual função você deseja testar?")
    opcao = int(input("Digite aqui: "))
    if opcao < 1 or opcao > 9:
        imprime_tracos()
        print("Digite uma opção válida")
        break
    elif opcao == 9:
        break
    else:
        imprime_tracos()
        texto = input("Digite aqui o texto que deseja testar: ")
        imprime_tracos()
        if opcao == 1:
            if lv.eh_texto_vogal(texto):
                print("Sim, o texto é formado apenas por vogais")
            else:
                print("Não, o texto não é formado apenas por vogais")
            imprime_tracos()
        elif opcao == 2:
            if lv.quantidade_vogais(texto) != 0:
                print("No seu texto tem", lv.quantidade_vogais(texto), "vogais")
            else:
                print("Seu texto não tem nenhuma vogal")
            imprime_tracos()
        elif opcao == 3:
            print("Seu texto sem as vogais fica: ", lv.remove_vogais(texto))
            imprime_tracos()
        elif opcao == 4:
            print("Seu texto depois de substituir as vogais ficou: ", lv.substitui_vogais(texto))
            imprime_tracos()
        elif opcao == 5:
            if lv.identifica_vogais(texto) != []:
                print("As vogais que tem no seu texto são: ", ", ".join(lv.identifica_vogais(texto)))
            else:
                print("Seu texto não tem vogais")
            imprime_tracos()
        elif opcao == 6:
            if lv.frequencia_vogais(texto) != []:
                print("A frequencia do seu texto é:")
                frequencia = lv.frequencia_vogais(texto)
                print("a/A", frequencia[0])
                print("e/E", frequencia[1])
                print("i/I", frequencia[2])
                print("o/O", frequencia[3])
                print("u/U", frequencia[4])
            else:
                print("Seu texto não tem vogais")
            imprime_tracos()
        elif opcao == 7:
            if lv.vogal_mais_frequente(texto) != []:
                print("A(s) vogal(is) que mais aparece(m) no seu texto: ", ", ".join(lv.vogal_mais_frequente(texto)))
            else:
                print("Seu texto não tem vogais")
            imprime_tracos()
        elif opcao == 8:
            if lv.sortear_vogal(texto) != "":
                print("Uma vogal aleatória do seu texto: ", lv.sortear_vogal(texto))
            else:
                print("Seu texto não tem vogais")
            imprime_tracos()
        continuar = input("Deseja continuar? (S/N): ")
        if continuar[0].lower() == "s":
            continue
        else:
            break
imprime_tracos()