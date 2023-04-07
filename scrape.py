import requests
from bs4 import BeautifulSoup

def web_content_div(web_content, class_path):
    web_content_div = web_content.find_all("div", {"class": class_path})
    try:
        spans = web_content_div[0].find_all("span")
        texts = [span.get_text() for span in spans]
    except IndexError:
        texts = []
    return texts
def hent_aksje_info(selskap):
    url = 'https://finance.yahoo.com/quote/'+ selskap +'?p=' + selskap + '&.tsrc=fin-srch'
    page = requests.get(url)
    #print(page.status_code)
    soup = BeautifulSoup(page.text, 'html.parser')
    req = requests.get(url)
    url_summary = 'https://money.cnn.com/quote/profile/profile.html?symb=' + selskap
  
    page_summary = requests.get(url_summary)
    soup2 = BeautifulSoup(page_summary.text, 'html.parser')
    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
    #print('Loading: ', url)
    #print(price)
    #print(hent_aksjepris(selskap))
    web_content = BeautifulSoup(req.text, "html.parser")
    texts = web_content_div(web_content, "D(ib) Va(m) Maw(65%) Ov(h)")
    if texts != []:
        change_dollar, change, info = texts[0], texts[1], texts[2]
    else:
        change_dollar, change, info = [], [], []
    pris = float(price)
    stock = {
        'company' : soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text,
        'symbol' : selskap,
        'price' : soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text,
        'change_percent' : change,
        'change_dollar' : float(change_dollar),
        'info' : info,
        'summary' : soup2.find('div', {'id': 'wsod_companyDescription'}).text
    }
    return stock





