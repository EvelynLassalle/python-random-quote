import random

def primary():
  #print("Keep it logically awesome.")

  try:
    with open("quotes.txt") as f:
      quotes = f.readlines()
      countNoQuotes = len(quotes)

      rnd = random.randint(0, countNoQuotes)
      print(quotes[rnd], end='')
  
  except FileNotFoundError:
    print("Unable to locate file <quotes.txt>")

  except Exception as e:
    print(e)

if __name__== "__main__":
	primary()		#llamada de la funcion
