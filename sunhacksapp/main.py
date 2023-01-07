import sunhacksapp.image_straighten as ims
import sunhacksapp.segmentation as sgm
import sunhacksapp.center_align as ca
import sunhacksapp.predict as pr
import re
import requests
from bs4 import BeautifulSoup

# import image_straighten as ims
# import segmentation as sgm
# import center_align as ca
# import predict as pr
# import re
# import requests
# from bs4 import BeautifulSoup

temp= "Paracetamol"

def disease_prediction(tab_name):
    r = requests.get("https://pharmeasy.in/search/all?name="+tab_name)
    soup = BeautifulSoup(r.content, 'lxml')
    a=soup.find("a",{"class":"ProductCard_medicineUnitWrapper__238qP ProductCard_defaultWrapper__3htqi"})
    URL="https://pharmeasy.in"+a['href']
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.findAll('td',{'class':'DescriptionTable_value__1afug'})
    uses = table[3].text
    uses = re.sub("and|or|with|due to", ",", uses)
    uses = uses.split(",")
    print('new format : ', uses)
    return uses

def ayurvedic_data(disease):
    url="https://ayuraarogyam.com/"
    desc=""
    resp=requests.get(url)
    soup=BeautifulSoup(resp.content,'html.parser')

    div=(soup.find("div",{"class":"wrappper"}).find("div",{"class":"wrapper-body-inner"}).find_all("div",{"class":"body-container"}))
    div_0=div[1].find("div",{"class":"homediseases"}).find_all("li")
    div_1=div[1].find("div",{"class":"hometraditional"}).find_all("li")
    div_2=div[1].find("div",{"class":"m-t-30 col-lg-3 col-md-4 col-sm-12 col-xs-12"}).find("ul",{"class":"accordion level1"}).find_all("li")

    list_1 = div_0 + div_1 + div_2

    nam,hrf=[],[]
    for i in list_1:
        n=i.find("a")
        hrf.append(n["href"])
        nam.append((n.text).strip("Ayurvedic Medicines For"))
    url_ = None
    illness= disease
    for i in range(0,len(nam)):
        if illness == nam[i]:
            url_=hrf[i]
            break
    
    if url_:
        resp=requests.get(url_)
        soup=BeautifulSoup(resp.content,'html.parser')

        Div=(soup.find("div",{"class":"products-brief"}).find_all("div"))  
        for i in range(0,len(Div)):
            p=Div[i].find_all("p")
            for j in range(0,len(p)):
                desc+=p[j].text
        return desc
    else:
        return "No data found"

def main(img_name, location, language):
    final_dict=dict()
    ims.main1(img_name)
    sgm.main(img_name)
    ca.main()
    final_dict['Prescriptions'] = pr.main()
    final_dict['Prescriptions'] = ["PARACETAMOL"]
    final_dict['Diseases'] = disease_prediction(temp)
    final_dict['Ayurvedic'] = ayurvedic_data(final_dict['Diseases'][0])
    print(final_dict)
    return final_dict


if __name__ == '__main__':
    main("c.jpeg", "Nashik", "Hindi")