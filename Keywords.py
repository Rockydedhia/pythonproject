import re
import xlsxwriter
import urllib.request
url = input('Enter a URl: ')
urllib.request.urlretrieve(url, 'bhavin.txt')

for line in open('bhavin.txt'):
    re.sub(
        '[@|<|.|>|.|!|.|:|.|;|.|{|.|}|.|</|.|"|.|-|.|#|.|(|.|)|.|,|.|"|.|=|.]', '', line)

print(line.readline())

 search_word = input("Enter a Keyword: ")
  count = 0
   if search_word in contents:
        ct = contents.count(search_word)
        book = xlsxwriter.Workbook('web.xlsx')
        sheet = book.add_worksheet()
        sheet.write('A1', 'Keywords')
        sheet.write('B1', 'Occur')
        sheet.write('A2', search_word)
        sheet.write('B2', ct)
        book.close()
        print('Your Record Save Succesfuly!!!')

    else:
        print('word not found')
