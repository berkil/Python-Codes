# Python-LAN-Scanner

Python code that will scan the lan network that the computer connected to 
and will retrive live PC's and open ports

This python code based on scapy, so you will have to download it (sudo apt-get install scapy).
If you forget to download scapy- the script will metion it to you!

You have to run this script as administrator (sudo).

This code retrives the network ip that you computer connected to, 
and by default it based on class C network (prefix 24).

If you wish to change the default prefix, go to line 25, and change the 'ip' variable.
'computer[x]' is the octets of the network- so you would like to change them!
i.e: my computer connected to 128.10.10.25 network, and this network is class B so line 25 should look like:
ip=computer[0]+'.'+computer[1]+'.0.0/16'

The port range by default is 1 to 200, if you want to chage this range. 
Change the numbers at line 49.
If you want it to scan specific port numbers you have to convert the range to list,
the line should look like this:
for port in [1,13,21,8080,443,53]:

At the end of the script a log file will be opened automatically with the list of livw PC's IP addresses and
open ports if any at all...
I 
