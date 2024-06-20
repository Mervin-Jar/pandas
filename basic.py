import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
ahh=[1,2,56,66]
myvar = pandas.DataFrame(mydataset)
print(myvar)
print(pandas.Series(mydataset))
print(pandas.Series(ahh, index=  ['a','b','c','d']))

