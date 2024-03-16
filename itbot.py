# Author: Leonid Krstevski

# Warning: This project is not intended for any cyber disruption or illegal purposes. The author is not responsible for any misuse of this code.

# Опомена: Овој проект не е наменет за било какви сајбер нарушувања или незаконски цели. Авторот не носи одговорност за било каква злоупотреба на овој код.

import random
import string
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import webbrowser
import tkinter as tk
from tkinter import messagebox

# Function to generate a random string of characters
def generate_random_string(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Function to generate a random email address
def generate_random_email():
    domain = "example.com"
    username = generate_random_string(10)  # Adjust the length as needed
    return f"{username}@{domain}"

# Registration function
def register_account():
    num_accounts = int(accounts_entry.get())
    num_processes = min(num_accounts, multiprocessing.cpu_count())

    # Create and start processes for registration
    processes = []
    for _ in range(num_processes):
        process = multiprocessing.Process(target=register_single_account)
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

    messagebox.showinfo("Процесот е успешен!", "Сите сметки се успешно создадени.")

    # Open the website after registration is completed
    webbrowser.open("https://krstevski-portfolio.000webhostapp.com/krstevski/index.html")

# Function to register a single account
def register_single_account():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://it.mk/registracija/")  # Open registration page
    
    try:
        # Accept cookies
        cookie_popup = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "cookie-law-info-bar")))
        accept_button = cookie_popup.find_element(By.CSS_SELECTOR, ".cli_action_button")
        accept_button.click()

        # Fill registration form
        username = generate_random_string()
        email = generate_random_email()
        password = generate_random_string()
        
        driver.find_element(By.ID, "reg_username").send_keys(username)
        driver.find_element(By.ID, "reg_email").send_keys(email)
        driver.find_element(By.ID, "reg_password").send_keys(password)

        # Submit the registration form
        driver.find_element(By.NAME, "register").click()

        # Wait for registration success
        WebDriverWait(driver, 10).until(EC.url_to_be("https://it.mk/"))

        # Save registration details to a text file
        with open("podatoci.txt", "a") as file:
            file.write("Автор: Леонид Крстевски / Author: Leonid Krstevski\n")  # Adding author name
            file.write(f"Корисничко име:/Username: {username}\nЕ-маил:/Email: {email}\nЛозинка:/Password: {password}\n\n")
            print("Податоците се успешно зачувани.")

    except Exception as e:
        print(f"Податоците се неуспешно зачувани: {str(e)}")

    finally:
        driver.quit()

# GUI setup
root = tk.Tk()
root.title("it.mk БОТ")

# Labels and Entry
tk.Label(root, text="Број на генерирани сметки:").pack()
accounts_entry = tk.Entry(root)
accounts_entry.pack()

# Register Button
register_button = tk.Button(root, text="Започни!", command=register_account)
register_button.pack()

# Author Information
author_label = tk.Label(root, text="Автор: Леонид Крстевски")
author_label.pack(side="bottom")

root.mainloop()

# Author: Leonid Krstevski

# Warning: This project is not intended for any cyber disruption or illegal purposes. The author is not responsible for any misuse of this code.

# Опомена: Овој проект не е наменет за било какви сајбер нарушувања или незаконски цели. Авторот не носи одговорност за било каква злоупотреба на овој код.
