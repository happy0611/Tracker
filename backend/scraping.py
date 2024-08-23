from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import requests
from urllib.parse import urljoin

# 定義するべき変数
amazonurl = "https://www.amazon.co.jp/gp/bestsellers/books/ref=zg_bs_books_sm"   
save_dir = r"C:\Users\user\Documents\Otoya\typescript\images"

def Bookscr():
    # Seleniumのセットアップ
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # ヘッドレスモード（ブラウザのUIを表示しない）
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    
    try:
        driver.get(amazonurl)
        time.sleep(5)  # ページが完全に読み込まれるまで待機

        # 画像と価格情報を取得
        imagetags = driver.find_elements(By.CSS_SELECTOR, "img.a-dynamic-image.p13n-sc-dynamic-image.p13n-product-image")
        span_tags = driver.find_elements(By.CSS_SELECTOR, "span._cDEzb_p13n-sc-price_3mJ9Z")

        for i in range(min(5, len(imagetags), len(span_tags))):
            image = imagetags[i]
            span = span_tags[i]

            img_url = image.get_attribute('src')
            if img_url and not img_url.startswith(('http://', 'https://')):
                img_url = urljoin(amazonurl, img_url)
            
            # 画像データを取得
            img_response = requests.get(img_url)

            # 画像の名前を生成
            img_name = os.path.join(save_dir, img_url.split('/')[-1])
            
            # 画像を保存
            with open(img_name, 'wb') as f:
                f.write(img_response.content)

            alt = image.get_attribute("alt")
            price = span.text.strip()

            print(f'{alt} {price} を保存しました。')

    finally:
        driver.quit()

Bookscr()
