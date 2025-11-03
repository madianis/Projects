while True:
        x=str.split(input("Fraction: "),'/')
        try:
              if len(x)==2:
                   y=int(x[1])
                   x=int(x[0])
                   if x<=y:
                         if (x/y) <= 0.01 :
                               print("E")
                         elif 0.99<=(x/y):
                               print("F")
                         else:
                               print(f"{x/y*100:.0f}%")
                         break

        except(ValueError,ZeroDivisionError):
              pass