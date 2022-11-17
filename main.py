sair=True
def Calc():
  global sair
  try:
    while sair==True:
      print("\n\nEscolha uma opção:\n\n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n\n0. Sair\n\n")
      op=int(input("Opção:"))
      if(op==0):
        sair=False
        continue

      v1=int(input("Valor 1:"))
      v2=int(input("Valor 2:"))

      if(op==1):
        print("\nResultado da Soma, "+str(v1)+"+"+str(v2)+", é "+str(v1+v2))
      elif(op==2):
        print("\nResultado da Subtração, "+str(v1)+"-"+str(v2)+", é "+str(v1-v2))
      elif(op==3):
        print("\nResultado da Multiplicação, "+str(v1)+"*"+str(v2)+", é "+str(v1*v2))
      elif(op==4):
        print("\nResultado da Divisão, "+str(v1)+"/"+str(v2)+", é "+str(v1/v2))
      else:
        print("Essa opção não existe!")
  except Exception as erro:
    print("Ocorreu um erro:\n\n" + str(erro))

Calc()