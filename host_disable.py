import sys

location = "C:\Windows\System32\drivers\etc\hosts"
#location = "demo_host.txt"


def block():

	with open(location,"a") as host:
		host.write("127.0.0.1	www.youtube.com\n")
		host.write("127.0.0.1	www.facebook.com\n")
		host.write("127.0.0.1	www.primevideo.com\n")

def unblock():

	with open(location,'r') as host:
		lines = host.readlines()

	with open(location,'w') as host:
		for line in lines:
			if line[:1] == '#':
				host.write(line)
			else:
				continue

def main():
	if len(sys.argv) == 2:
		#then do some thing
		if sys.argv[1] == "-b":
			block()
		elif sys.argv[1] == "-ub":
			unblock()
	else:
		print("1 argument expected \n")
		print("-b : block\n")
		print("-ub : unblock\n")
		exit(1)


if __name__ == '__main__':
    main()