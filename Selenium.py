from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://demoqa.com/')
elementsButton = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div/div[1]')
elementsButton.click()

checkBoxButton = driver.find_element_by_xpath('//*[@id="item-1"]')
checkBoxButton.click()


checkBox = driver.find_element_by_xpath('//*[@id="tree-node"]/ol/li/span/label/span[1]')
checkBox.click()


radiobuttonButton = driver.find_element_by_xpath('//*[@id="item-2"]')
radiobuttonButton.click()

radiobutton_impressive= driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]')
radiobutton_impressive.click()

radiobutton_Yes= driver.find_elements_by_id("yesRadio")
radiobutton_Yes.click()
