from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/tables")
time.sleep(2)
rows = driver.find_elements(
    By.XPATH, "//table[@id='table1']/tbody/tr"
)

search_name = "Smith"

found = False

for row in rows:

    columns = row.find_elements(By.TAG_NAME, "td")

    row_data = [column.text for column in columns]

    print(row_data)
    if search_name in row_data:

        print("\nPerson found!")
        print("Name:", search_name)


        print("Email:", row_data[2])
        print("Due:", row_data[3])

        found = True
        break

assert found, f"{search_name} was not found in the table"

print("\nAssignment 5 completed successfully!")

driver.quit()