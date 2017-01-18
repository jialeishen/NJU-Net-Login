#!/usr/bin/python
#coding:utf8
# Login the campus network of Nanjing University automatically
# Login page: http://p.nju.edu.cn
# Author: Jialei Shen
# E-mail: shenjialei1992@163.com
# Latest: 2017.01.18
 
import urllib
import os
import time

def check_network():
    check_code_one = os.system('ping -w 1 -n 1 223.5.5.5 > nul')
    check_code_two = os.system('ping -w 1 -n 1 114.114.114.114 > nul')
    if check_code_one == 0 or check_code_two == 0:
        return 0
    return 1

def print_ts(message):  
        print "[%s] %s"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), message)
 
if __name__ == '__main__':
    interval = 10
    print_ts("-"*50)
    print_ts ('Author: Jialei Shen') 
    print_ts ('E-mail: shenjialei1992@163.com')
    print_ts ('Latest: 2017.01.18')
    print_ts ('')  
    print_ts("Check the Internet every %s seconds."%interval)  
    print_ts("-"*50)
 
    # Your username and password
    username = "mg1234567"
    password = "XXXXXXXX"
 
    post_data = {
        "username": username,
        "password": password,
    }
    post_data = urllib.urlencode({'username': username, 'password': password}).encode('utf-8')
    login_url = "http://p.nju.edu.cn/portal_io/login"
     
    while True:
        if check_network():
            print_ts("Internet NOT connected! Connecting now...")
            urllib.urlopen(login_url, post_data)
        print_ts("Internet connected!")
        print_ts("Checking Internet connection...")
        time.sleep(interval)  # Check interval, herein 10s
