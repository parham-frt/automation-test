from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
from selenium.webdriver.common.keys import Keys

service = Service(executable_path=binary_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)
base_url = ("https://dineshvelhal.github.io/testautomation-playground")
driver.get(f"{base_url}/forms.html")
driver.find_element('id','check_javascript').click()
checke1 = driver.find_element('id','check_validate').text
assert checke1 == "JAVASCRIPT"
driver.find_element('id','notes').send_keys("helo test2")
checke2 = driver.find_element('id','area_notes_validate').text
assert checke2 == "helo test2"
assert checke2 == "ershad"
