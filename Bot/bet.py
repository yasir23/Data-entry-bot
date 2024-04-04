import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def read_excel_data(file_path):
    # Load the Excel file
    df = pd.read_excel("C:\\Users\\Yasir\\Downloads\\Student profile 2023-24 Nodo Jokhio.xlsx")
    return df

 # This will print the DataFrame as a table
def setup_selenium(webdriver_path, target_url):
    # Setup WebDriver
    driver = webdriver.Chrome(".\\vk_swiftshader.dll")
    driver.get("https://emis.sef.edu.pk/#/school/students/save-student")
    return driver




def submit_student_info(driver, student_data):
    # Assuming student_data is a dict with keys matching the form's input names
    for key, value in student_data.items():
        if isinstance(value, list):  # Check if the value is a list (for multiple values)
            for val in value:
                input_field = driver.find_element(By.NAME, key)
                input_field.clear()
                input_field.send_keys(val)
                time.sleep(1)  # Optional: wait a bit between inputs
        else:
            input_field = driver.find_element(By.NAME, key)
            input_field.clear()
            input_field.send_keys(value)
    # Find and click the submit button
    submit_button = driver.find_element(By.ID, "submit_button_id")  # Adjust ID as necessary
    submit_button.click()
    time.sleep(2)  # Wait for submission to process