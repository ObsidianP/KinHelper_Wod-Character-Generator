import requests
from bs4 import BeautifulSoup
import random
import re

namelist = []
extractlist = []
url='https://www.behindthename.com/names/language/english/'
class extractor:
#@param: url string default 
#@return: Boolean based on if text file was able to be created from site html
   def __init__(*args):
      try:
         with open("namegen.txt",'r') as file:
            file.close
      except OSError:
         print('namegen.txt not generated. Scraping data...')
         for url in args:
            if  'behindthename' in website:
               for x in 17:
                  url += '/'+str(x)
                  requests.get(url)
                

               
          
      
          
      # for site in args:
      #       if 'https://www.behindthename.com/' in site:
      #          url = 'https://www.behindthename.com/'

               
#       url += str(random.randrange(0,17))
#       print('extracting html from '+url)
#       response = requests.get(url)
#       try:
#          match response.status_code:
#             case 200:
#                with open('webpage.txt', 'w', encoding="utf-8") as file:
#                   file.write(response.text)
#                   print('webpage saved as textfile \"webage.txt\"')
#                   file.close
#                   return True
#             case __:
#                print('site returned code '+code)
#                return False
#       except Exception:
#          print('An error has occured: '+Exception)
#          return False

# #@param: None
# #@Return: random shuffled list[]
# def extract_names():
#    print("extracting names from text file...")
#    try:
#       with open('webpage.txt','r', encoding="utf-8") as textfile:
#         for line in textfile:
#            if re.search("name/[A-z]*\"",line) == None:
#               continue
#            elif re.match("Apply this search to the user-submitted names",line) != None:
#               print("ending extraction")
#               break
#            else:
#               extractlist = list(set(re.findall("name/[A-z]*\"",line)))
     
#         for extract in extractlist:
#            name = str(extract)
#            name = name.replace('\"','')
#            name = str.capitalize(name.replace('name/',''))
#            namelist.append(name)
         
#         textfile.close
#         # print(name_list)
#         random.shuffle(namelist)
#         return namelist
#    except TypeError:
#       print('extracted webpage text file not found, extracting webpage')
#       check = extract_webage()
#       if check:
#          extract_names()
#       else:
#          print('Could not extract website data')
