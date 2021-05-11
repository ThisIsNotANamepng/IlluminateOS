import webbrowser
print ("This will take a minute to load, but you will have a fully-functioning copy of firefox in your browser")
c = webbrowser.get('firefox')
  
c.open_new_tab('https://duckduckgo.com/')

import main
