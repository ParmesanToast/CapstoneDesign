from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome 드라이버 경로 설정
chrome_driver_path = "path_to_chromedriver"

# Selenium 웹드라이버 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # GUI 없이 실행
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Chrome 웹드라이버 실행
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# 대상 페이지로 이동
driver.get("https://velog.io/search?q=%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%A9%B4%EC%A0%91")

# 페이지가 완전히 로드될 때까지 기다림
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "xpath_of_the_element")))

# 동적으로 생성된 콘텐츠 가져오기
dynamic_content = driver.find_element(By.XPATH, "xpath_of_the_element").text
print(dynamic_content)

# 웹드라이버 종료
driver.quit()
