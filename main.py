from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# Auto-installs the correct ChromeDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get("https://www.bmkg.go.id/kualitas-udara/pm25")
# print(driver.title)

# By CSS Selector (most flexible)
# el = driver.find_element(By.CSS_SELECTOR, "h1.title")







# table_list = [['City', 'Time', 'PM2.5', 'Category']]
# for i in range(1, 99):
#     # # By XPath
#     try:
#         el = driver.find_element(By.XPATH, f'//*[@id="__nuxt"]/main/div[2]/div/div/a[{i}]/div[2]')
#         table_list.append(el.text.split("\n"))
#     except:
#         break
#     # print(type(el.text))
#     # print(el.text.split("\n"))
#     # append the data to the dataframe

# df = pd.DataFrame(table_list[1:], columns=table_list[0])


driver.get("https://www.bmkg.go.id/cuaca/prakiraan-cuaca/31.72.01")
el = driver.find_element(By.XPATH, f'//*[@id="__nuxt"]/main/div[1]/div[2]/div[2]')
content = el.text.split("\n")
content.remove(content[0])
waktu = list(content[0].split(" "))
content.remove(content[0])


list_waktu = []

while True:
    try:
        list_waktu.append(f'{waktu[0]} {waktu[1]} {waktu[2]}')
        waktu.pop(0)
        waktu.pop(0)
        waktu.pop(0)
    except:
        break
print(list_waktu)

while True:
    try:
        kecamatan = content.pop(0)
        # print(kecamatan)

        data_cuaca = []
        for i in range(0,29,3):
            data_cuaca.append([kecamatan, list_waktu[0], content[0], content[1], content[2]])
            content.remove(content[0])
            content.remove(content[0])
            content.remove(content[0])
            list_waktu.remove(list_waktu[0])
        print(data_cuaca)
    except:
        print("done")
        break

print(content)

# print(df)
# # By ID, class, tag name
# el = driver.find_element(By.ID, "main-content")
# el = driver.find_element(By.CLASS_NAME, "card")
# el = driver.find_element(By.TAG_NAME, "table")
# # Find multiple elements (returns a list)
# items = driver.find_elements(By.CSS_SELECTOR, ".product-card")
driver.quit()  # Always close the browser when done
