text = "python"

# Slicing -> forward
print(text[1:4])

# Slicing -> backward
print(text[1:4:-1]) # empty 
print(text[-1:-4:-1]) # noh
print(text[-4:-6:-1]) # ty 
print(text[4:1:-1]) # oht 

print(text[5:2]) # empty
print(text[5:2:-1]) # noh
print(text[10]) # Indexing -> IndexError: string index out of range
print(text[10:]) # noh
