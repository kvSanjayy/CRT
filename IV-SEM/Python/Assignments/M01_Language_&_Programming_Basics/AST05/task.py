from typing import List


def Collatz_Sequence(n: int)-> List:
   sequence = [n]

   while n != 1:
      if n % 2 == 0:      # even number
            n = n // 2
      else:               # odd number
            n = 3 * n + 1

      sequence.append(n)

   return sequence
    
   
if __name__ == '__main__':
    n = int(input())
    print(Collatz_Sequence(n))