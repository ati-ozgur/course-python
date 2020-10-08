## Recursion means that function calls itself

def recursion(N):
  pass
  # we should have exit condition
  # if exit_condition_true:
  #   exit the function
  # else:
  #   do something
  #   change the N argument, should be so that exit condition eventually will be true
  #   call itself


def count_down2(n):
    if n < 0:
      return
    else:
      print(n)
      n = n -1
      count_down2(n)

count_down2(5)

