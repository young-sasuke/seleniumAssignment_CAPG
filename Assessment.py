# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=opts)


# # driver.get("https://demowebshop.tricentis.com")
# # time.sleep(2)

# # driver.find_element("xpath", "//a[contains(text(),'Books')]").click()
# # time.sleep(2)

# # driver.find_element("xpath", "(//input[@value='Add to cart'])[1]").click()
# # time.sleep(2)

# # driver.find_element("xpath", "//span[text()='Shopping cart']").click()
# # time.sleep(2)

# # product = driver.find_element("xpath", "//td[@class='product']")
# # print("Product in cart:", product.text)

# #####-----------------------TASK 2-----------------------

# # driver.get("https://demowebshop.tricentis.com")
# # time.sleep(2)

# # driver.find_element("xpath", "//a[contains(text(),'Electronics')]").click()
# # time.sleep(5)

# # driver.find_element("xpath", "//a[contains(text(),'Cell phones')]").click()

# #####-----------------------TASK 3-----------------------

# # driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# # time.sleep(2)

# # driver.find_element("xpath", "//button[text()='Start']").click()

# # time.sleep(6)

# # text = driver.find_element("xpath", "//div[@id='finish']/h4").text
# # print("Text displayed:", text)
# #####-----------------------TASK 4-----------------------

# # driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# # time.sleep(2)

# # driver.find_element("xpath", "//button[text()='Remove']").click()
# # time.sleep(5)

# # driver.find_element("xpath", "//button[text()='Add']").click()

# #####-----------------------TASK 5-----------------------

# # driver.get("https://demoqa.com/select-menu")
# # time.sleep(2)

# # driver.find_element("xpath", "//div[@id='withOptGroup']").click()
# # time.sleep(2)

# # driver.find_element("xpath", "//div[text()='Group 2, option 1']").click()
# # time.sleep(2)

# # value = driver.find_element("xpath", "//div[contains(@class,'singleValue')]").text

# # print("Selected value:", value)

# #####-----------------------TASK 6-----------------------

# # driver.get("https://demoqa.com/select-menu")
# # time.sleep(2)

# # driver.execute_script("window.scrollBy(0,600)")
# # time.sleep(2)

# # multi = Select(driver.find_element("xpath", "//select[@id='cars']"))

# # multi.select_by_visible_text("Volvo")
# # multi.select_by_visible_text("Saab")
# # multi.select_by_visible_text("Opel")

# # for option in multi.all_selected_options:
# #     print(option.text)

# #####-----------------------TASK 7-----------------------

# # driver.get("https://demoqa.com/menu/")
# # time.sleep(2)

# # action = ActionChains(driver)

# # main = driver.find_element("xpath", "//a[text()='Main Item 2']")
# # action.move_to_element(main).perform()
# # time.sleep(2)

# # sub = driver.find_element("xpath", "//a[text()='SUB SUB LIST »']")
# # action.move_to_element(sub).perform()
# # time.sleep(2)

# # item = driver.find_element("xpath", "//a[text()='Sub Sub Item 1']")
# # item.click()

# #####-----------------------TASK 8-----------------------

# # driver.get("https://demoqa.com/droppable")
# # time.sleep(3)

# # drag = driver.find_element("xpath", "//div[@id='draggable']")
# # drop = driver.find_element("xpath", "//div[@id='droppable']")

# # action = ActionChains(driver)

# # action.click_and_hold(drag).move_to_element(drop).release().perform()

# # time.sleep(2)

# # result = driver.find_element("xpath", "//div[@id='droppable']").text
# # print(result)

# #####-----------------------TASK 9-----------------------

# # driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# # time.sleep(2)

# # driver.find_element("xpath", "//button[text()='Click for JS Confirm']").click()

# # alert = driver.switch_to.alert
# # alert.accept()

# # result = driver.find_element("xpath", "//p[@id='result']").text
# # print(result)

# #####-----------------------TASK 10-----------------------

# # driver.get("https://the-internet.herokuapp.com/upload")
# # time.sleep(2)

# # driver.find_element("xpath", "//input[@id='file-upload']").send_keys("C:\\Users\\KIIT\\Desktop\\Assessment\\test.txt")

# # driver.find_element("xpath", "//input[@id='file-submit']").click()

# # print(driver.find_element("xpath", "//h3").text)
