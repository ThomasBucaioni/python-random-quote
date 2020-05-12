import random
last = 13
rnd = random.randint(0, last)
def mainfunction():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes[13])

if __name__== "__main__":
  mainfunction()
