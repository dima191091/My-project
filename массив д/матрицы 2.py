dict = {'a': 1, 'b': 2, 'c': 3}
try:
    a = dict['f']
except KeyError:
  print()
except IndexError:
  print()
finally:
    print()