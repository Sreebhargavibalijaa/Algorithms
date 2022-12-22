# The Luhn algorithm, also known as the modulus 10 or mod 10 algorithm, is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers, IMEI numbers
def luhn_Algorithm(s):
  '''Function to check whether given credit card number is valid or not'''
  n= len(s)
  sum=0
  for i in range(n):
    output=0
    if (i%2!=0):
      output = (2*int(s[i]))
      if (output >9):
        first_digit = output%10
        second_digit =  (output//10)%10
        output = first_digit + second_digit
      sum = sum+output
    else:
      sum = sum+ int(s[i])
  print(sum)
  return (True if sum%10==0 else False)

luhn_Algorithm("79927398713")