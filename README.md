# SSH-brute-force

## Overview

Aim of this project is to create a script to perform login brute forcing using SSH. We will be using the PWN module to interact with the SSH service. The Paramiko module will be used for error handling.

Password list:
[100.txt](https://github.com/WillieStevenson/top-100-passwords/blob/master/password-list.txt)


## Specifics:

- Virtual Machine (VirtualBox) with [Kali Linux](https://www.kali.org/get-kali/#kali-virtual-machines)
- Python 3.0

## Text Editor:

- [Sublime Text](https://www.sublimetext.com/docs/linux_repositories.html)

## Python Modules Used:

- [Pwntools](https://docs.pwntools.com/en/stable/)
- [Paramiko]([https://docs.python.org/3/library/sys.html)
  
## What I Learned:

- **Try**: I got a better understanding as to why try is used here, as we will be iterating over potentially hundreds of passwords. Instead of stopping after one wrong match, I can continue using try.
- **SSH()**: Pretty straightforward, creates an SSH connection with the specified IP.
- **Connected()**: Returns true if the SSH connection is connected.
- **Close()**: Closes the SSH connection.
- `sudo systemctl start ssh`: How else do you make an SSH connection? Didn't realize SSH needed to be enabled on the host prior to the connection. DUH.
- **paramiko.ssh_exception.AuthenticationException**: Exception raised when authentication failed for some reason. It may be possible to retry with different credentials.


## Learning References

- [Python Try Except - W3Schools](https://www.w3schools.com/python/python_try_except.asp)
- [Pwntools SSH Documentation](https://docs.pwntools.com/en/stable/tubes/ssh.html#pwnlib.tubes.ssh.ssh)
- [Top 100 Passwords - GitHub](https://github.com/WillieStevenson/top-100-passwords/blob/master/password-list.txt)

