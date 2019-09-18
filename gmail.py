from selenium import webdriver

driver = webdriver.Chrome('/media/hitesh/New Volume/python/programm/experiment/gmail_automation/chromedriver')
driver.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

email = input('Enter your email id : ')
pas = input('Enter your password : ')

msg_box = driver.find_element_by_xpath('//input[@id = "identifierId"]')
msg_box.send_keys(email)

nextS = driver.find_element_by_xpath('//div[@id = "identifierNext"]')
nextS.click()

password = driver.find_element_by_xpath('//input[@type = "password"]')
password.send_keys(pas)

nextSt = driver.find_element_by_xpath('//div[@id = "passwordNext"]')
nextSt.click()