from captive import get_captcha
from uuid import uuid4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

URL = "https://servicos.receita.fazenda.gov.br/Servicos/certidao/CNDConjuntaInter/InformaNICertidao.asp?tipo=2"
IMGID = uuid4().hex

def get_sample(url, id="imgCaptchaSerpro"):
    driver = webdriver.Chrome()
    driver.get(url)
    img = driver.find_element_by_id(id)
    capt = get_captcha(driver, img, f"data/sample_{id}_{IMGID}.png")

if __name__ == "__main__":
    get_sample(URL)
    