def result(x):
  if x=='1' or x=='4' or x=='78' :
      return '+'
  elif x[len(x)-1]=='5':
      return  '-'
  elif x[0]=='9':
      return '*'
  else:
      return '?'

if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        x = (input())
        print(result(x))
