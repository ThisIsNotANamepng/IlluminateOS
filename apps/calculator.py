# Copyright 2016 -- Levi Starrett & Jay Hankins
# for educational purposes only
# Calculator -- a four function calculator commandline tool
def add(a, b):
  return a + b
def sub(a, b):
  return a - b
def mult(a, b):
  return a * b
def div(a, b):
  return a / b
a = None
b = None
op = None
while (True):
  # get input values
  a = input("Enter the first argument: ")
  op = input("Enter the operation: ")
  b = input("Enter the second argument: ")
  try:
      a = int(a)
      b = int(b)
  except ValueError:
      print ("Invalid number argument...")
      op = None

  # decide function
  if (op != None):
      if (op == "+"):
          print ("Sum: ", add(a, b))
      elif (op == "-"):
          print ("Difference: ", sub(a, b))
      elif (op == "*"):
          print ("Product: ", mult(a, b))
      elif (op == "/"):
          print ("Quotient: ", div(a, b))
      else:
          print ("Invalid operation...")

  q = input("Quit? [y/n] ")
  if (q == "y" or q == "Y"):
      import main
      appmenu()
