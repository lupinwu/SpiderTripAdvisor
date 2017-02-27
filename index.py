from bs4 import BeautifulSoup
import requests
import time

url = 'http://www.tripadvisor.cn/Attractions-g60763-Activities-c47-New_York_City_New_York.html'
urls = ['http://www.tripadvisor.cn/Attractions-g60763-Activities-c47-oa{}-New_York_City_New_York.html'
        '#ATTRACTION_LIST'.format(str(i)) for i in range(30, 400, 30)]
urls.insert(0, url)


def get_attractions(url, data=None):
    response = requests.get(url)
    # time.sleep(2)  # 每隔2秒请求一次,防止反爬虫
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.select('div.property_title > a[target="_blank"]')
    imgs = soup.select('img[width="160"]')
    cates = soup.select('div.p13n_reasoning_v2')
    for title, img, cate in zip(titles, imgs, cates):
        data = {
            'title': title.get_text(),
            'img': img.get('src'),
            'cate': list(cate.stripped_strings),
        }
        print(data)


for single_url in urls:
    get_attractions(single_url)

"""
# 收藏页爬取,由于js无法实现
url_saves = 'https://www.tripadvisor.cn/Saves/272263'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    'Cookie': 'TAUnique=%1%enc%3AAQutONkiXiArI%2FXHbSYwT8T3HFQ9ZCN6cOJ%2BIsJ5iMs2jHwltRJPGQ%3D%3D; __gads=ID=c30456eb0c19d6ca:T=1460534051:S=ALNI_MauG_CUSWVwtjlFpMB6NezOAd5njw; TAPD=tripadvisor.cn; bdshare_firstime=1461126676896; taMobileRV=%1%%7B%2210028%22%3A%5B60763%5D%7D; ServerPool=B; TASSK=enc%3AAJ6O4MKObq0C3xPDHG86pejTC38AimMNShsuiTu8aTxNOr%2BS4ZkrCVeyXYZnro4yVdzeNdbPN2dzS5KaArCwTt%2FcoKORc%2BC%2F%2Bp%2FDUF533oapjqxe7EuwTkjc0%2BYzX0vuEA%3D%3D; VRMCID=%1%V1*id.18061*llp.%2F-a_suppm%5C.-a_supkw%5C.20749484436-a_supbl%5C.%257BlocalInfo%257D-a_supbc%5C.0-a_supsc%5C.1-a_supap%5C.1cl1-a_supbt%5C.-m18061-a_supai%5C.6405077608-a_supci%5C.95827891*e.1488724980441; _jzqy=1.1488120182.1488120182.1.jzqsr=baidu|jzqct=www%2Etripadvisor%2Ecn.-; _jzqckmp=1; CommercePopunder=SuppressAll*1488120545497; _smt_uid=570dfb23.1c9d8fcf; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.60763_57l105127_57*RS.1; CM=%1%HanaPersist%2C%2C-1%7CPremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C6%2C-1%7CTheForkMCCPers%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCCSess%2C%2C-1%7CCpmPopunder_2%2C3%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7C%24%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C17%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CSaveFtrPers%2C%2C-1%7Cpers_rev%2C%2C-1%7CTheForkRRSess%2C%2C-1%7CMetaFtrSess%2C%2C-1%7Cmds%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CFtrSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7Cbookstickcook%2C%2C-1%7Csh%2C%2C-1%7CLastPopunderId%2C137-1859-null%2C-1%7Cpssamex%2C%2C-1%7C2016sticksess%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7C2016stickpers%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7Cbookstickpers%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttraction_Review-g60763-d105127-Reviews-Central_Park-New_York_City_New_York.html; SecureLogin2=3.4%3AAOqzYNVwCVsr2FRS2yBCFHVbH8mMKP0O6PARfKscSmOJgSlhLsJgyMC%2FH2FvjaLh0uX4zNgFMG0uLT2MX52OfXhhHoYprlEMrf8VwALCR4ueDA%2BBrvk%2FBijSYc1vmaQ2W%2BsvhdvPmiAurr%2FfdFwd8VS1lSqTaIpXF0qxsFLgb9fsttcoi1dYDLYKaqOTnVP%2FGVSYlo7JTPEaMsiXUYYwla8%3D; TAAuth2=%1%3%3A1d8bb63b6b8fcc485d08da8a2e3fd9bf%3AAOokYd6WirRliR12SzzCnZZejgrOHNN7bJzo1cAckef3Lsz7xl4vwbhoojb7U%2FyWmGvop0hl%2FbqKVQqL39kb6%2FBl9bvkqo1snKr1L%2BbEUyE0e8kWVufLrF%2Bk62T65Ia5zd0vEi2wh1nXdmAOPyy%2FxeGsgZtibo2MgesBko9i%2FDmxFiyApb5EmkRt%2BR8VCsIY%2B0NJaerQN%2FztThHfgDNeUjGKlG7zS2FVrPNt8Yt%2BoGil; roybatty=TNI1625!ANa7mCG5AYIwjNi0hDvJ4jBJz4pxsFZY5xrLvlbwHoxKriZDmT%2F7nmZAU2a1Kv%2BlIFGbkip5H6Uy0msg1xyhgfBtjtoTK1CQ1kU2rAHZ9ujEKMfiId4SBPSSxxm5EExwhI58iuAKZ2Mt8uC0vx7oyNXCbD4Qs5fIovVtwN3zSffQ%2C1; TASession=%1%V2ID.3D503BD0C59B6528B3FF9DC2A89CDE06*SQ.73*MC.18061*LR.https%3A%2F%2Fwww%5C.baidu%5C.com%2Fbaidu%5C.php%3Fsc%5C.aamK00jlPafFvOTzvhfZ-3fgxLE3QcY_ogjagRbVxAwqHmYwL7z0ySYCN6jdYzjYGwPmm0P0tuJHFGZ1GQL4zCvK716jG2uwB4khNgSpjpf5e4WjkMihP1DDYnkO_FSbNJ99PzyXewFVS-jZiD0goOkwev3eTmvVa8zdR3smTxd8aXG226%5C.7Y_a9nOA1Iqj3LHTbZxikg__lpS_XjZaqWx8vu5ZuE*LP.%2F-a_suppm%5C.-a_supkw%5C.20749484436-a_supbl%5C.%257BlocalInfo%257D-a_supbc%5C.0-a_supsc%5C.1-a_supap%5C.1cl1-a_supbt%5C.-m18061-a_supai%5C.6405077608-a_supci%5C.95827891*LS.ActionRecord*GR.30*TCPAR.70*TBR.41*EXEX.67*ABTR.2*PPRP.83*PHTB.98*FS.25*CPU.67*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.A742A412067143EBAA8E54380B9379D8*LF.zhCN*FA.1*DF.0*IR.3*OD.zh*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.105127; TAUD=LA-1488120180439-1*LG-67229818-2.1.F.*LD-67229819-.....; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1488120182,1488120204,1488120298; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1488187410; _jzqa=1.91843995079239870.1460534052.1488156577.1488187411.12; _jzqc=1; _jzqx=1.1488156577.1488187411.2.jzqsr=tripadvisor%2Ecn|jzqct=/attractions-g60763-activities-c47-new_york_city_new_york%2Ehtml.jzqsr=tripadvisor%2Ecn|jzqct=/attraction_review-g60763-d105127-reviews-central_park-new_york_city_new_york%2Ehtml; _qzja=1.1696067475.1460534051941.1488156576902.1488187410565.1488158609253.1488187410565..0.0.70.12; _qzjb=1.1488187410565.1.0.0.0; _qzjc=1; _qzjto=7.2.0; _jzqb=1.1.10.1488187411.1; ki_t=1460534564175%3B1488187412408%3B1488187412408%3B5%3B62; ki_r=',
}


def get_favs(url, data=None):
    response = requests.get(url_saves, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.select('a.location-name')
    imgs = soup.select('div.photo > div.sizedThumb > img.photo_image')
    metas = soup.select('span.format_address')

    if data == None:
        for title, img, meta in zip(titles, imgs, metas):
            data = {
                'title': title.get_text(),
                'img': img.get('src'),
                'meta': list(cate.stripped_strings),
            }
            print(data)
"""
