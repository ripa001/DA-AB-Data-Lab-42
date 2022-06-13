from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://projects.intra.42.fr/projects/list')
content = driver.page_source
driver.find_element(by=By.XPATH, value='//*[@id="user_login"]').send_keys("<Intra Username>")
driver.find_element(by=By.XPATH, value='//*[@id="user_password"]').send_keys("<Intra Password>")
driver.find_element(by=By.XPATH, value='//*[@id="new_user"]/div[2]/input').click()
time.sleep(5)
ul = driver.find_elements(by=By.XPATH, value='//*[@id="projects-list-container"]/ul/li')
d = {'Project Name': [], 'Experience': [], "Project Duration": []}
for li in ul:
	d["Project Name"].append(li.find_element(by=By.CLASS_NAME, value='project-name').text)
	d["Experience"].append(li.find_element(by=By.CLASS_NAME, value='project-difficulty').text)
	d["Project Duration"].append(li.find_element(by=By.CLASS_NAME, value='project-duration').text)
df = pd.DataFrame(d)
df.to_csv("datasets/intra-projects.csv")
