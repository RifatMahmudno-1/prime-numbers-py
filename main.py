from asyncio.windows_events import INFINITE
import math


def isPrime(num):
  sqrt = math.floor(math.sqrt(num))
  for i in range(2, sqrt + 1):
    if num % i == False:
      return False
  return num > 1


def autoFind():
  for i in range(0, INFINITE):
    res = isPrime(i)
    if res:
      print(i, "is a prime number.")


def main():
  print("What do you want to do?")
  print("Select one from below =>")
  print("1) Check if it's a prime number.")
  print("2) Auto find prime numbers.")
  sel = input()
  if sel != "1" and sel != "2":
    print("Invalid selection. Type either 1 or 2")
  if sel == "1":
    print("Provide your number")
    num = input()
    try:
      num = int(num)
    except:
      num = False
    if num == False:
      print("Excepted only numbers.")
    else:
      res = isPrime(num)
      if res:
        print(num, "is a prime number")
      else:
        print(num, "isn't a prime number")
      ext = input("Press anykey and Enter to exit\n")
      if ext or not ext:
        return False
  if sel == "2":
    autoFind()


main()
