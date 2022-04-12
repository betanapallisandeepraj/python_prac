import subprocess
#for loop with 4 variables to ping all IPs in a list
upper_bound = 256
for i in range(1,upper_bound):
	for j in range(0,upper_bound):
		for k in range(0,upper_bound):
			for l in range(0,upper_bound):
				ip = f"{i}.{j}.{k}.{l}"
				#print(f"pinging {ip}")
				process = subprocess.Popen(['ping', '-c 1', '-W 100', '-i 0.01', ip], stdout=subprocess.PIPE, universal_newlines=True)
				var=""
				for output in process.stdout.readlines():
					var=var+output
				abc=[]
				abc=abc+var.splitlines()
				print(abc[1],abc[2])

#private ip ranges are as below, 
#which can be used by anyone in local networks for free
#10.0.0.0 — 10.255.255.255;
#172.16.0.0 — 172.31.255.255; 
#192.168.0.0 — 192.168.255.255
#public ip's are not free, one has to purchase. So you can skip checking private ip for respose.
