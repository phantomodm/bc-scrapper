# from lxml import html
# import requests

# page = requests.get('http://localhost:3000/catchers-mitt-one-color-quick-order/')
# tree = html.fromstring(page.content)

# radio = tree.xpath('/[@class="form-radio"]/*')

# print radio


from bs4 import BeautifulSoup
import requests

page_array = [
    'http://localhost:3000/catchers-mitt-one-color-quick-order/',
    'http://localhost:3000/catchers-mitt-dual-color-quick-order/',
    'http://localhost:3000/catchers-mitt-tri-color-quick-order/',
    'http://localhost:3000/first-base-mitt-tri-color-quick-order/',
    'http://localhost:3000/first-base-mitt-dual-color-quick-order/',
    'http://localhost:3000/first-base-mitt-one-color-quick-order/',
    'http://localhost:3000/infield-glove-one-color-quick-order/',
    'http://localhost:3000/infield-glove-dual-color-quick-order/',
    'http://localhost:3000/infield-glove-tri-color-quick-order/'
]

elements = ["Body Color:", "Glove Logo Colors:"]
objArray = []
attributeName = ''
def save(obj,file,mode):
    with open(file,mode) as edit:
        edit.write(str(obj))
        edit.write(str(',\n'))

for page in page_array:

    r = requests.get(page)
    data = r.text
    soup = BeautifulSoup(data,'lxml')
    final = {}
    final2 = {}
    for link in soup.find_all('input', class_='form-radio'):
        obj = {}
        color = {}
        #print(link.get_attribute_list('value')[0])
        obj["name"] = link.get_attribute_list('name')[0]
        obj["id"] = link.get_attribute_list('id')[0]
        obj["value"] = link.get_attribute_list('value')[0]
        objArray.append(obj)
        # for elm in elements:
        #     for parent in link.find_previous_siblings('label'):
        #         label = parent.contents[0].strip()
        #         if label == elm:
        #             print("yes")
        # if link.get('class')[0] == 'form-radio':
        #     print(link.get('class'))
        # for parent in link.find_previous_siblings('label'):
        #     print(parent.contents[0])
save(objArray,"attr.json",'a')