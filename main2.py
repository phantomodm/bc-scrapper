from bs4 import BeautifulSoup
import itertools
import requests
import pyrebase

fireBaseConfig = {
    
}

# Firebase initialization
firebase = pyrebase.initialize_app(fireBaseConfig)
fbRef = firebase.database()

page_array = [
    'http://localhost:3000/catchers-mitt-one-color-quick-order/',
    'http://localhost:3000/catchers-mitt-dual-color-quick-order/',
    'http://localhost:3000/catchers-mitt-tri-color-quick-order/',
    'http://localhost:3000/first-base-mitt-tri-color-quick-order/',
    'http://localhost:3000/first-base-mitt-dual-color-quick-order/',
    'http://localhost:3000/first-base-mitt-one-color-quick-order/',
    'http://localhost:3000/infield-glove-one-color-quick-order/',
    'http://localhost:3000/infield-glove-dual-color-quick-order/',
    'http://localhost:3000/infield-tri-color-quick-order/',
    'http://localhost:3000/infield-web-change-quick-order/',
    'http://localhost:3000/first-base-mitt-one-color-quick-order/',
    'http://localhost:3000/catchers-mitt-web-change-quick-order/',
    'http://localhost:3000/infield-glove-trim-change-quick-order/',
    'http://localhost:3000/infield-dual-welt-glove-trim-change-quick-order/',
    'http://localhost:3000/infield-dual-welt-glove-one-color-quick-order/',
    'http://localhost:3000/infield-dual-welt-glove-tri-color-quick-order/'
]

elements = ["Body Color:","Glove Accent Colors:","Glove Trim Colors",  "Glove Logo Colors:"]
objArray = []
templates = {
    "one-color-glove": {
        "body": ["_x5F_rngo", "_x5F_bfg","_x5F_rngi", "_x5F_pnko", "_x5F_pnki", "_x5F_mid", "_x5F_indi", "_x5F_plm", "_x5F_thbo", "_x5F_wst","_x5F_indo", "_x5F_thbi","_x5F_thb","_x5F_wlt", "_x5F_bnd", "_x5F_stch", "_x5F_web", "_x5F_lce","_x5F_tgt","_x5F_dwmid"],
        "accent": [],
        "trim": [],
        "logo": ["_x5F_logo", "_x5F_fgrl"]
    },
    "trim-color-glove": {
        "body": ["_x5F_rngo", "_x5F_bfg","_x5F_rngi", "_x5F_pnko", "_x5F_pnki", "_x5F_mid", "_x5F_indi", "_x5F_plm", "_x5F_thbo", "_x5F_wst","_x5F_indo", "_x5F_thbi","_x5F_thb", "_x5F_web", "_x5F_lce","_x5F_tgt"],
        "accent": [],
        "trim": ["_x5F_bnd","_x5F_wlt","_x5F_stch","_x5F_dwmid"],
        "logo": ["_x5F_logo", "_x5F_fgrl"]
    },
    "dual-color-glove": {
        "body": ["_x5F_rngo", "_x5F_rngi","_x5F_bfg", "_x5F_pnko", "_x5F_pnki", "_x5F_mid", "_x5F_indi", "_x5F_plm", "_x5F_thbo", "_x5F_indo", "_x5F_thbi"],
        "accent": ["_x5F_web", "_x5F_wst","_x5F_mid","_x5F_dwmid"],
        "trim": ["_x5F_wlt", "_x5F_bnd", "_x5F_stch", "_x5F_lce"],
        "logo": ["_x5F_logo", "_x5F_fgrl"]
    },
    "tri-color-glove": {
        "body": ["_x5F_rngo", "_x5F_bfg","_x5F_rngi", "_x5F_pnko", "_x5F_pnki", "_x5F_mid", "_x5F_indi", "_x5F_plm", "_x5F_thbo", "_x5F_wst"],
        "accent": ["_x5F_indo", "_x5F_thbi","_x5F_mid"],
        "trim": ["_x5F_wlt", "_x5F_bnd", "_x5F_stch", "_x5F_web", "_x5F_lce"],
        "logo": ["_x5F_logo", "_x5F_fgrl"]
    },
    "one-color-mitt":{
        "body": ["_x5F_wst", "_x5F_stch", "_x5F_lce", "_x5F_bfg","_x5F_thb","_x5F_tgt","_x5F_utoe","_x5F_plm","_x5F_bnd"],
        "accent": [],
        "trim": [],
        "logo": ["_x5F_logo", "_x5F_fgrl"]
    },
    "dual-color-mitt": {
        "body": ["_x5F_wst", "_x5F_bnd", "_x5F_stch", "_x5F_lce", "_x5F_bfg", "_x5F_thb", "_x5F_tgt"],
        "accent": ["_x5F_utoe","_x5F_plm"],
        "trim": [],
        "logo": ["_x5F_logo", "_x5F_fgrl"]
    },
    "tri-color-mitt": {
        "body": ["_x5F_wst", "_x5F_bfg", "_x5F_thb", "_x5F_plm"],
        "accent": ["_x5F_utoe","_x5F_web","_x5F_tgt"],
        "trim": ["_x5F_lce", "_x5F_bnd", "_x5F_stch"],
        "logo": ["_x5F_logo", "_x5F_fgrl"]
    },
    "mitt-lace-change": {
        "body": ["_x5F_wst", "_x5F_bnd", "_x5F_bfg","_x5F_thb","_x5F_utoe","_x5F_plm","_x5F_tgt"],
        "accent": [],
        "trim": ["_x5F_lce", "_x5F_stch"],
        "logo": ["_x5F_logo", "_x5F_fgrl"]
    },
    "web-change-glove": {
        "body": ["_x5F_wst", "_x5F_wlt", "_x5F_bfg", "_x5F_mid", "_x5F_bnd", "_x5F_stch", "_x5F_lce", "_x5F_rngo", "_x5F_rngi", "_x5F_pnko", "_x5F_pnki", "_x5F_mid", "_x5F_indi", "_x5F_plm", "_x5F_thbo", "_x5F_indo", "_x5F_thbi","_x5F_dwmid"],
        "accent": ["_x5F_web"],
        "trim": [],
        "logo": ["_x5F_logo", "_x5F_fgrl"]
    },
    "web-change-mitt": {
        "body": ["_x5F_wst", "_x5F_wlt", "_x5F_bfg", "_x5F_utoe", "_x5F_thb", "_x5F_stch", "_x5F_tgt", "_x5F_bnd"],
        "accent": ["_x5F_web"],
        "trim": [],
        "logo": ["_x5F_logo", "_x5F_fgrl"]
    }


}

designTemplate ={}

radioValue = ''
radioName = ''
radioId = ''
swatchName = ''

def save(obj,file,mode):
    with open(file,mode) as edit:
        edit.write(str(obj))
        edit.write(str(',\n'))


for page in page_array:
    r = requests.get(page)
    data = r.text
    soup = BeautifulSoup(data,'lxml')
    #labelsTag = soup.find_all('label','form-label form-label--alternate form-label--inlineSmall')
    labelsTag = soup.find_all('div',class_="form-field")
    profiles = soup.find_all('dd', class_="productView-info-value")
    product = soup.find_all('input' )
    product_id = ''
    for p in product:
        if p.get_attribute_list('name')[0] == 'product_id':
            product_id = p.get_attribute_list('value')[0]

    design = ''
    print('Connecting to {0} .....'.format(page))
    for profile in profiles:
        if "mitt" in profile.contents[0] or "glove" in profile.contents[0]:
            print('Design is {}.'.format(profile.contents[0]))
            design = profile.contents[0]
            designTemplate = dict(**templates[design])


    for labels in labelsTag:

        label = labels.find_all('label',class_="form-label form-label--alternate form-label--inlineSmall")
        colorString = labels.find_all('label', class_="form-option form-option-swatch")        

        for title in label:
            section = title.contents[0].strip()
            radioSection = title.find_all_next('input', class_='form-radio')
            for radio,color in itertools.izip(radioSection,colorString):
                
                swatch = color.find_next('span', class_="form-option-variant form-option-variant--color")
                for elm in elements:
                    if elm == section:
                        
                        obj = {}
                        obj["product_id"] = product_id
                        obj["designTemplate"] = design
                        obj["name"] = radio.get_attribute_list('name')[0]
                        obj["id"] = radio.get_attribute_list('id')[0]
                        obj["value"] = radio.get_attribute_list('value')[0]
                        obj["color"] = swatch.get_attribute_list('title')[0]
                        obj["hex"] = swatch.get_attribute_list('style')[0].split(' ')[1].strip()
                        obj["build"] = designTemplate

                        objArray.append(obj)


save(objArray,"attr.json",'a')
for attrib in objArray:
    print('Adding product {} to backend'.format(attrib["product_id"]))
    profilesRef = fbRef.child('nine-positions-glove-profile/{}'.format((attrib["product_id"])))
    profileRef = profilesRef.push({
        'product_id': attrib["product_id"],
        'designTemplate': attrib["designTemplate"] ,
        'attribute_name': attrib["name"],
        'attribute_id': attrib["id"],
        'attribute_value': attrib["value"],          
        'attribute_color': attrib["color"],
        'attribute_hexColor': attrib["hex"],
        'build':  attrib["build"]
    })



