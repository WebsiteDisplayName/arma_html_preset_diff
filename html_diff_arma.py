
# Importing BeautifulSoup class from the bs4 module 
from bs4 import BeautifulSoup 
  
# Opening the html file
# existing_op_falling_water.html
# new_op_falling_water.html

file_1_name = r"Op_Falling_Water_manually_added"
file_2_name = r"Op_Falling_Water"

def ret_mod_names(html_name: str) -> None:
  HTMLFile = open(html_name+".html", "r") 
    
  # Reading the file 
  index = HTMLFile.read() 
    
  # Creating a BeautifulSoup object and specifying the parser 
  S = BeautifulSoup(index, 'lxml') 
    
  # Using the find_all method to find all elements of a tag 
  with open(html_name + '.txt', 'w') as f:
    for tag in S.find_all('td', {'data-type': 'DisplayName'}): 
        f.write(f'{tag.text}\n')
  
  return None

ret_mod_names(file_1_name)
ret_mod_names(file_2_name)

file_1_txt = open(file_1_name+".txt","r")
file_2_txt = open(file_2_name+".txt","r")
list_1 = file_1_txt.readlines()
list_2 = file_2_txt.readlines()

print("file_1_unique")
list_1_unique = [print(mod_name, end='') for mod_name in list_1 if mod_name not in list_2]

print("\nfile_2_unique")
list_2_unique = [print(mod_name, end='') for mod_name in list_2 if mod_name not in list_1]