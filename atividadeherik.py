print("quanto tempo falta para vc se alistar")
idade = int(input("sua idade: "))

if idade > 18:
    print(f"o alistamento obrigatorio deve ser feito com 18 anos, vc ta a {idade-18} anos atrasado.")
elif idade == 18:
    print("vc esta com a idade exata para se alistar, acesse o site alistamento.eb.mil.br para mais informações.")
elif idade < 18:
    print(f"vc ainda nao ta na idade para se alistar. O alistamento so acontece quando vc completa 18 anos, espere mais {18-idade} anos para se alistar.")