import random

f = open("quotes.txt", "a")
f.write("I'm adding this quote with computer magic")
f.write("\n")
f.close()

def primary():
   for i in range(5):
      f = open("quotes.txt")
      quotes = f.readlines()
      f.close()
      last = 16
      rnd = random.randint(0, last)
      print(quotes[rnd], end='')

if __name__== "__main__":
  primary()
