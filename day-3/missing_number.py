def find_missing(lst1, lst2):
  if lst1 == lst2 == []:
    return 0
  elif lst1 == lst2:
    return 0
  else:
    missing = [val for val in lst2 if val not in lst1]
    if missing:
      return missing[0]