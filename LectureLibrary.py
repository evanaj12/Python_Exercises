
#Lecture Notes on 16 Oct 2013

def is_prime (n):
  limit = int (n ** 0.5) + 1
  for divisor in range (2, limit):
    if (n % divisor == 0):
      return False
  return True

def sum_digits (n):
  sum = 0
  while (n > 0):
    sum += n % 10
    n = n // 10
  return sum

def reverse (n):
  rev_num = 0
  while (n > 0):
    rev_num = rev_num * 10 + (n % 10)
    n = n // 10
  return rev_num

def is_palindromic (n):
  return (n == reverse (n))

def sub_string(st):
  st = input ('Enter a string: ')
  len_str = len(st)
  window = len_str
  while (window > 0):
    startIndex = 0
    while (startIndex + window <= len_str):
      print (st[startIndex : startIndex + window])
      startIndex += 1
    window = window - 1

def main ():
  # Test is_prime() function
  for i in range (2, 20):
    if (is_prime(i)):
      print (i)

  # Test sum_digits() function
  print (sum_digits (1234))

  # Test reverse() function
  x = 91827
  print (x, reverse (x))

  # Test is_palindromic () function
  x = 123454321
  if (is_palindromic (x)):
    print (x, 'is palindromic')
  else:
    print (x, 'is not palindromic')

  # Find a non-palindromic number whose cube is palindromic
  for n in range (1000, 10000):
    if (not is_palindromic(n)):
      n3 = n * n * n
      if (is_palindromic (n3)):
        print (n, n3)
	break

  # Find a prime which when added to its reversal is prime
  for n in range (100, 1000):
    if (is_prime (n)):
      rev_num = reverse (n) + n
      if (is_prime (rev_num)):
        print (n, rev_num)
        break

main()
