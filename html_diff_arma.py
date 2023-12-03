
# Importing BeautifulSoup class from the bs4 module 
from bs4 import BeautifulSoup 
  
# Opening the html file
# existing_op_falling_water.html
# new_op_falling_water.html
input_html = r"new_op_falling_water"
HTMLFile = open(input_html+".html", "r") 
  
# Reading the file 
index = HTMLFile.read() 
  
# Creating a BeautifulSoup object and specifying the parser 
S = BeautifulSoup(index, 'lxml') 
  
# Using the find_all method to find all elements of a tag 
with open(input_html + '.txt', 'w') as f:
  for tag in S.find_all('td', {'data-type': 'DisplayName'}): 
      f.write(f'{tag.text}\n')