import pandas as pd
import numpy as np

from libfinder import libraryfinder,get_lib_name,get_lib_version


print("Library name : ",get_lib_name())
print("Library versions : ",get_lib_version)


lib=libraryfinder()


#Get the lib versions
print("libraryfinder class library versions :",lib.get_lib_version())

#save the lib in txt file
lib.to_txt("requirement3.txt")



