import time

from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from seleniumwire.utils import decode
import json

driver = webdriver.Chrome()
driver.get('https://www.bing.com/translator?from=ko&to=en')
search_query = driver.find_element(By.ID, "tta_input_ta")
# print("Enter the string")
# fromString = input()
fromString = "양극재"

time.sleep(1)
search_query.send_keys(fromString)

time.sleep(1)

for request in driver.requests:
    if request.response.status_code == 200:
        strContentType = str(request.response.headers['Content-Type'])
        if strContentType.__contains__("application/json"):
            strBody = str(decode(request.response.body, request.response.headers.get('Content-Encoding', 'identity')))
            if strBody.__contains__("detectedLanguage") & strBody.__contains__("translations"):
                json_list = json.loads(strBody[2:-1])
                json_object = json_list[0]
                print(json_object["translations"][0]["text"])

time.sleep(2)