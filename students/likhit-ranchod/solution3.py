#problem 1

s={"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
count=0
for x in s:
    if x=="a":
        count=count+1
    elif x=="e":
        count=count+1
    elif x=="i":
        count=count+1
    elif x=="o":
        count=count+1
    elif x=="u":
        count=count+1
    else:
        continue 
print(count)

#problem 2


s={"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
count=0
for x in s:
  if x=="b":
      count=count+1
  elif x=="c":
      count=count+1
  elif x=="d":
      count=count+1
  elif x=="f":
      count=count+1
  elif x=="g":
      count=count+1  
  elif x=="h":
      count=count+1
  elif x=="j":
      count=count+1
  elif x=="k":
      count=count+1
  elif x=="l":
      count=count+1
  elif x=="m":
      count=count+1
  elif x=="n":
      count=count+1
  elif x=="p":
      count=count+1
  elif x=="q":
      count=count+1
  elif x=="r":
      count=count+1
  elif x=="s":
      count=count+1
  elif x=="t":
      count=count+1
  elif x=="v":
      count=count+1
  elif x=="w":
      count=count+1
  elif x=="x":
      count=count+1
  elif x=="y":
      count=count+1
  elif x=="z":
      count=count+1
  else:
      continue
print(count)

#problem 3

s={"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
total_vowels = 0
total_consonants = 0
vowels_ref = "aeiou"

for letter in s:
    if letter in vowels_ref:
        total_vowels = total_vowels + 1
    else:
        total_consonants = total_consonants + 1
        
print("Total Vowels:", total_vowels)
print("Total Consonants:", total_consonants)
