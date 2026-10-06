anos_exp = float(input("Anos de experiência na área:"))

if anos_exp >= 5:
    print("Categoria: desenvolvedor sênior")
elif anos_exp >= 2:
    print("Categoria: desenvolvedor pleno")
else:
    print("Categoria: desenvolvedor júnior")