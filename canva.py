from selenium import webdriver
import time
import random
import string

#winfo-bin (404942 atau 522149)

#random string untuk email
def get_random_string(length):
    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for i in range(length))
    return username
nama_random = get_random_string(6)


#default password dan email
pw = ('netwozam207')
imel = ('@bapaklo.com')



#Membuka Browser
driver = webdriver.Chrome('C:\chromedriver.exe')
driver.get("https://www.canva.com/signup")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="root"]/div/main/div[6]/div/section/div/div/div/div/div/div/button').click()
time.sleep(2)

#proses daftar
print("\nLoading..........")
nama = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[6]/div/section/div/div/div/div/div/div/div[2]/form/div[1]/input')
nama.send_keys(nama_random)

email = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[6]/div/section/div/div/div/div/div/div/div[2]/form/div[2]/div/div/div/input')
email.send_keys(nama_random,imel)

password = driver.find_element_by_xpath('//*[@id="root"]/div/main/div[6]/div/section/div/div/div/div/div/div/div[2]/form/div[3]/input')
password.send_keys(pw)
time.sleep(2)

#klik daftar dan menuju payment
driver.find_element_by_xpath('//*[@id="root"]/div/main/div[6]/div/section/div/div/div/div/div/div/div[2]/form/button/span').click()
time.sleep(5)
driver.find_element_by_xpath("//h5[contains(text(), 'Personal')]").click()
time.sleep(5)
driver.find_element_by_xpath("//p[contains(text(), 'Poster')]").click()
time.sleep(5)
driver.find_element_by_xpath("//span[contains(text(), 'Try Canva Pro')]").click()
time.sleep(10)
driver.find_element_by_xpath("//span[contains(text(), 'Get it free for 30 days')]").click()



#Proses Manual dan pembuatan akun jika payment berhasil
print("\nSilahkan Selesaikan Payment dan Captcha.......")
time.sleep(10)
print("\nPastikan Status Payment Anda Sebelum Melanjutkan")
pilih = input("\nApakah Payment Anda Berhasil ? (Y/N) : ")
time.sleep(1)
if pilih == "Y" or "y":
    canva=open("canva.txt", "a+")
    canva.write(nama_random)
    canva.write(imel)
    canva.write("\n")
    print("Berhasil")
elif pilih ==  "N" or "n":
    print("Coba Lagi gan")
else:
    exit()