import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
 from csv import reader
 from hashlib import sha256
 hash_password_to_password = {}
 for password in range(1000,10000):
    hashing_number = sha256(b'%i' % password).hexdigest()
    hash_password_to_password[hashing_number] = password
 with open(input_file_name) as f:
    psswords_singer = reader(f)
    
    with open(output_file_name,'w', newline='') as w:    
     saver=csv.writer(w)
     for row in psswords_singer:
        name_users = row[0]
        for key in row[1:]:
         saver.writerow([name_users, str(hash_password_to_password[key])])