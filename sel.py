from selenium import webdriver
from selenium.webdriver.common.keys import Keys

d = webdriver.Chrome()
d.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
d.implicitly_wait(10)
elem = d.find_element_by_id("identifierId")

elem.send_keys('ajlawless7991@gmail.com')
elem.send_keys(Keys.RETURN)

elem = d.find_element_by_name('password')

elem.send_keys("7204852076")
elem.send_keys(Keys.RETURN)
