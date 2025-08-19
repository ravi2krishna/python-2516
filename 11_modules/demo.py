# Importing Of Modules

# 1st Approach -> whole module
import math
print(math.sqrt(25))

# 2nd Approach  -> specific functionality in module
from math import sqrt
print(sqrt(25))

# Optional -> can use alias names as well for easy readability
import math as m 
print(m.sqrt(25))