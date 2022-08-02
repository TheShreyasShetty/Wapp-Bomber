from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager 

def banner():
    print('''
		_______________________________________________________
    ____       __     _   _    ____     _____    ____  
    /   )    /    )   /  /|    /   )    /    '   /    )
---/__ /----/----/---/| /-|---/__ /----/__------/___ /-
  /    )   /    /   / |/  |  /    )   /        /    |  
_/____/___(____/___/__/___|_/____/___/____ ___/_____|__
                                                       
    ''')


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://web.whatsapp.com/')

    name = input('Enter the name of user or group: ')
    msg = input('Enter your message: ')
    count = int(input('Enter the count: '))

    input('Enter any key after scanning QR code')

    user = driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[18]/div')
    user.click()

    # The classname of message box may vary //span[@title = "{}"]'.format(name)
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')

    for i in range(count):
        msg_box.send_keys(msg)
        # The classname of send button may vary.
        button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span')
        button.click()
    print('Bombing Complete!!')


banner()
main()
