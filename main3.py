from bs4 import BeautifulSoup
import itertools
import requests

page_array = [
    'http://localhost:3000/catchers-mitt-one-color-quick-order/']

elements = ["Body Color:", "Glove Logo Colors:"]
objArray = []
attributeName = ''

def save(obj,file,mode):
    with open(file,mode) as edit:
        edit.write(str(obj))
        edit.write(str(',\n'))





for page in page_array:
    #print(objArray)
    r = requests.get(page)
    data = r.text
    soup = BeautifulSoup(data,'lxml')
    labelsTag = soup.find_all('div',class_="form-field")
    optionDiv = soup.find_all('label',class_="form-label form-label--alternate form-label--inlineSmall")
    radioValue = ''
    radioName = ''
    radioId = ''
    swatchName = ''
    obj = {}
    for elm in elements:
        
        for labels in optionDiv:
            if labels.contents[0].strip() == elm:
                
                radioSection = labels.find_all_next('input', class_='form-radio')
                
                color = labels.find_all_next('span', class_="form-option-variant form-option-variant--color")
                for radio, colorHex in itertools.izip(radioSection,color):
                    
                    radioValue = radio.get_attribute_list('value')
                    radioName = radio.get_attribute_list('name')
                    radioId = radio.get_attribute_list('id')
                    swatchName = colorHex.get_attribute_list('title')
                    print(radioName)
                    obj["name"] = radioName[0]
                    # obj["id"] = radioId
                    # obj["value"] = radioValue
                    # obj["color"] = swatchName
                    objArray.append(obj)
print(obj)
#print(objArray)
save(objArray,"attr1.json",'a')


