import google

print ("If it doesen't work, try 'pip install google' in the shell")
try:
    from googlesearch import search
except ImportError: 
    print("No module named 'google' found")
  
# to search
query = input("Search:  ")
  
for j in search(query, tld="co.in", num=10, stop=50, pause=2):
    print(j)




import main
mainmenu()