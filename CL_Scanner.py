#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import urllib
from headers import *
from vulnz import *

print ga.green+'''
                                     ▄████▄      ██▓    
                                    ▒██▀ ▀█     ▓██▒    
                                    ▒▓█    ▄    ▒██░    
                                    ▒▓▓▄ ▄██▒   ▒██░    
                                    ▒ ▓███▀ ░   ░██████▒
                                    ░ ░▒ ▒  ░   ░ ▒░▓  ░
                                      ░  ▒      ░ ░ ▒  ░
                                    ░             ░ ░   
                                    ░ ░             ░  ░
                                    ░                   

        ****************************************************************************
        *|  By Criminal Laoin                                                      *
        *|  Remote Code/Command Execution, XSS, SQL Injection Scanner              *
        *|  Instagram: Criminal.laoin / Criminal_Laoin                             *
        *|  Twitter: Criminal_Laoin                                                *
        *|  Telegram: Criminal_laoin                                               *
        *|  TurkHackTeam: Criminal Laoin                                           *
        ****************************************************************************
        '''+ga.end

def urls_or_list():
	url_or_list = raw_input(" [!] Tek site veya liste? [1/2]: ")
	if url_or_list == "1":
	 	 url = raw_input(" [!] Hedef URL'yi girin: ")
		 
		 if "?" in url:
		 	rce_func(url)
		 	xss_func(url)
		 	error_based_sqli_func(url)
		 else:
			print ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" Geçerli bir URL değil"+ga.end			
			print ga.red +" [Warning] Tam URL yazmalısınız http://site.com/page.php?id=value \n"+ ga.end
			exit()
	if url_or_list =="2":
		 urls_list = raw_input( ga.green+" [!] Liste ismini girin [list.txt]: "+ga.end)
		 open_list = open(urls_list).readlines()
		 for line in open_list:
			 if "?" in line:
			 	links = line.strip()
		  	 	url = links
		  	 	print ga.green+" \n [!] Hedef Taraniyor %s"%url +ga.end
		  	 	rce_func(url)
			 	xss_func(url)
			 	error_based_sqli_func(url)
			 else:
			 	links = line.strip()
		  	 	url = links
				print ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" Geçerli bir URL değil"+ga.end				
				print ga.red +" [Warning] Tam URL yazmalısınız http://site.com/page.php?id=value \n"+ ga.end
		 exit()				

urls_or_list()





