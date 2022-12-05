#!/usr/bin/python
# -*- coding:utf8 -*-
# Generate Strong Password List For BruteForce Attack

from time import sleep

j = 0
file = open('passlist.txt','w')
name_list = []
last_name_list = []
first_name_list = []
special_number = ['!','@','#','$','%','^','&','*','?','_','-','+','=']
faverate_number = ['0','1','2','3','4','5','6','7','8','9','10',
					'20','2020','100','12','123','1234','12345',
					'123456','1234567','12345678','123456789']
print(75*"=")
print("  _____        _____ _               _               _      _     _   ")
sleep(0.1)
print(" |  __ \      / ____| |             | |             | |    (_)   | |  ")
sleep(0.1)
print(" | |__) |   _| (___ | |__   __ _  __| | _____      _| |     _ ___| |_ ")
sleep(0.1)
print(" |  ___/ | | |\___ \| '_ \ / _` |/ _` |/ _ \ \ /\ / / |    | / __| __|")
sleep(0.1)
print(" | |   | |_| |____) | | | | (_| | (_| | (_) \ V  V /| |____| \__ \ |_ ")
sleep(0.1)
print(" |_|    \__, |_____/|_| |_|\__,_|\__,_|\___/ \_/\_/ |______|_|___/\__|")
sleep(0.1)
print("         __/ |                                                        ")
sleep(0.1)
print("        |___/                                                         ")
sleep(0.1)
print(75*"=")
print("""
Generate Strong Password List For BruteForce Attack
Created By MiladGol (https://github.com/miladgol/pyshadowlist)
""")
print(75*"=")
sleep(0.5)

first_name = input("First Name: ")
last_name = input("Last Name: ")
birthday = input("Birthday (1970/05/19): ")
phone_number = input("Phone Number (9990002211): ")
special_name = input("Special Name (cat,dog): ")

f1_number = phone_number[:3]
f2_number = phone_number[3:6]
f3_number = phone_number[6:]
year = birthday[2:4]
years = birthday[:4]
month = birthday[5:7]
day = birthday[8:]

first_name = first_name.lower()
first_name_1 = first_name.replace(first_name[0], first_name[0].upper())
first_name_2 = first_name.upper()
last_name = last_name.lower()
last_name_1 = last_name.replace(last_name[0], last_name[0].upper())
last_name_2 = last_name.upper()

if special_name != '':
	name_list = special_name.split(",")

name_list.append(first_name)
name_list.append(first_name_1)
name_list.append(first_name_2)
name_list.append(last_name)
name_list.append(last_name_1)
name_list.append(last_name_2)

first_name_list.append(first_name)
first_name_list.append(first_name_1)
first_name_list.append(first_name_2)
last_name_list.append(last_name)
last_name_list.append(last_name_1)
last_name_list.append(last_name_2)

for fn in first_name_list:
	for ln in last_name_list:
		name_list.append(fn + ln)

for name in name_list:
	file.write("{0}\n".format(name))
	file.write("{0}\n".format(name + year))
	file.write("{0}\n".format(name + years))
	file.write("{0}\n".format(name + day + month + year))
	file.write("{0}\n".format(name + f1_number))
	file.write("{0}\n".format(name + f2_number))
	file.write("{0}\n".format(name + f3_number))
	file.write("{0}\n".format(name + phone_number))
	j += 8
	for item in special_number:
		file.write("{0}\n".format(name + item))
		file.write("{0}\n".format(name + item + year))
		file.write("{0}\n".format(name + item + years))
		file.write("{0}\n".format(name + item + day + month + year))
		file.write("{0}\n".format(name + item + f1_number))
		file.write("{0}\n".format(name + item + f2_number))
		file.write("{0}\n".format(name + item + f3_number))
		file.write("{0}\n".format(name + item + phone_number))
		j += 8
		for spc_num in faverate_number:
			file.write("{0}\n".format(name + spc_num))
			file.write("{0}\n".format(name + item + spc_num))
			j += 2

file_size = file.seek(0, 2)
print("\nFile Created! => Number Of Password: {0} , size: {1}".format(j, file_size))
file.close()
