import random

def primary():
   # print("Keep it logically awesome.")
   for i in range(5):
      f = open("quotes.txt")
      quotes = f.readlines()
      f.close()
      last = 15
      rnd = random.randint(0, last)
      print(quotes[rnd], end='')

if __name__== "__main__":
  primary()
