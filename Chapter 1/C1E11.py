year = (2017,2003,2011,2005,1987,2009,2020,2018,2009)

#to access value at index -3
print(f"The value at index -3 is {year[-3]}")
print("\n")

#original and reversed tuple order
print("original order is", year)
reverse = year[:: -1]
print(f"reversed tuple is", reverse)
print("\n")

#times 2009 appears
twothousandnine = year.count(2009)
print(f"2009 appears {twothousandnine} times in the tuple.")
print("\n")

#index of 2018
twentyeighteen = year.index(2018)
print(f"The index of 2018 is {twentyeighteen}.")
print("\n")

#length of tuple
length = len(year)
print(f"Length of the tuple is {length}.")