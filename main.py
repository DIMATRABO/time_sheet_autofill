from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import json
import os


url = 'http://apebsint.tmsa.ma:8005/OA_HTML/AppsLocalLogin.jsp?requestUrl=http%3A%2F%2Fapebsint.tmsa.ma%3A8005%2FOA_HTML%2FOA.jsp%3Fpage%3D%2Foracle%2Fapps%2Ffnd%2Fframework%2Fnavigate%2Fwebui%2FNewHomePG%26homePage%3DY%26OAPB%3DFWK_HOMEPAGE_BRAND%26oapc%3D2%26transactionid%3D1034799422%26oas%3DHhZoYe1VFDXcRuQ0WLJZfA..&cancelUrl=http%3A%2F%2Fapebsint.tmsa.ma%3A8005%2FOA_HTML%2FAppsLogin&langCode=F'  # Replace with the URL of your login page
url2 = 'http://apebsint.tmsa.ma:8005/OA_HTML/RF.jsp?function_id=16744&resp_id=58760&resp_appl_id=809&security_group_id=0&lang_code=F&oas=FAR0_h6H5RwMTVPdZPWnuQ..&params=.K0.2qGTNapbIVSNL1pBGAnAy7Nf2s1FRaPFxKLvPl4'

json_file_path = "time.json"


username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
username = 'a.ait benha'
password = 'CIRES@202402'

chrome_options = Options()
chrome_options.add_argument('--disable-javascript')

driver = webdriver.Chrome(options=chrome_options)



driver.get(url)

username_input = driver.find_element(By.ID, value='usernameField')  # Replace 'username' with the actual name attribute of the username input field
password_input = driver.find_element(By.ID, value='passwordField')  # Replace 'password' with the actual name attribute of the password input field
submit_button = lement_with_message = driver.find_element(By.CSS_SELECTOR, '[message="FND_SSO_LOGIN"]')  


# Fill in the login form
username_input.send_keys(username)
password_input.send_keys(password)

# Submit the login form
submit_button.click()
time.sleep(1)
driver.get(url2)
############### form #################


with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

i=0
# Loop over the list of dictionaries in the JSON data
for entry in data:
    i+=1
    # Find form elements and fill them using the data from the current dictionary
    driver.execute_script("arguments[0].removeAttribute('onkeypress')", driver.find_element(By.NAME, 'A24'+str(i)+'N1display'))
    driver.execute_script("arguments[0].removeAttribute('onkeyup')", driver.find_element(By.NAME, 'A24'+str(i)+'N1display'))
    driver.execute_script("arguments[0].removeAttribute('onchange')", driver.find_element(By.NAME, 'A24'+str(i)+'N1display'))


    driver.execute_script("arguments[0].removeAttribute('onkeypress')", driver.find_element(By.NAME, 'A25'+str(i)+'N1display'))
    driver.execute_script("arguments[0].removeAttribute('onkeyup')", driver.find_element(By.NAME, 'A25'+str(i)+'N1display'))
    driver.execute_script("arguments[0].removeAttribute('onchange')", driver.find_element(By.NAME, 'A25'+str(i)+'N1display'))


    driver.execute_script("arguments[0].removeAttribute('onkeypress')", driver.find_element(By.NAME, 'A26'+str(i)+'N1display'))
    driver.execute_script("arguments[0].removeAttribute('onkeyup')", driver.find_element(By.NAME, 'A26'+str(i)+'N1display'))
    driver.execute_script("arguments[0].removeAttribute('onchange')", driver.find_element(By.NAME, 'A26'+str(i)+'N1display'))

    projet_input = driver.find_element(By.ID, 'A24'+str(i)+'N1display')
    projet_input.send_keys(entry['projet'])
    time.sleep(0.01)

    tache_input = driver.find_element(By.ID, 'A25'+str(i)+'N1display')
    tache_input.send_keys(entry['tache'])
    time.sleep(0.01)

    type_input = driver.find_element(By.ID, 'A26'+str(i)+'N1display')
    type_input.send_keys(entry['type'])
    time.sleep(0.01)


    lundi_input = driver.find_element(By.ID, 'B22_'+str(i)+'_0')
    lundi_input.send_keys(entry['lundi'])
    time.sleep(0.01)

    mardi_input = driver.find_element(By.ID, 'B22_'+str(i)+'_1')
    mardi_input.send_keys(entry['mardi'])
    time.sleep(0.01)

    mercredi_input = driver.find_element(By.ID, 'B22_'+str(i)+'_2')
    mercredi_input.send_keys(entry['mercredi'])
    time.sleep(0.01)


    jeudi_input = driver.find_element(By.ID, 'B22_'+str(i)+'_3')
    jeudi_input.send_keys(entry['jeudi'])
    time.sleep(0.01)

    vendredi_input = driver.find_element(By.ID, 'B22_'+str(i)+'_4')
    vendredi_input.send_keys(entry['vendredi'])
    time.sleep(0.01)

    samedi_input = driver.find_element(By.ID, 'B22_'+str(i)+'_5')
    samedi_input.send_keys(entry['samedi'])
    time.sleep(0.01)

    dimanche_input = driver.find_element(By.ID, 'B22_'+str(i)+'_6')
    dimanche_input.send_keys(entry['dimanche'])
    time.sleep(0.01)

 



Continuer_button = driver.find_element(By.ID, "review")  
Continuer_button.click()

time.sleep(1000)  # Sleep for 10 seconds

# Add a delay (for demonstration purposes)

# Close the browser
driver.quit()
