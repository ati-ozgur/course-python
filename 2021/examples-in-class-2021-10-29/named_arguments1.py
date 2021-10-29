def named_arguments1(a,b,c):
    print(f"a {a},b {b}, c {c}")


named_arguments1(a=1, b= 2,c = 3)

named_arguments1(b=2, c=3, a=1)

named_arguments1(b=2, a=1, c=3)


named_arguments1(2, c=1, b=3)


#named_arguments1(2, a=1, b=3)
# TypeError: named_arguments1() got multiple values for argument 'a'

# named_arguments1(2, b=1)
# TypeError: named_arguments1() missing 1 required positional argument: 'c'

