host = open("/etc/hosts", 'a')
list_of_websites = {'coep':'www.coep.org.in', 'youtube':'www.youtube.com', 'facebook':'www.facebook.com', 'google':'www.google.com', 'linkedin':'www.linkedin.com', 'wikipedia':'www.wikipedia.org'}

name = str(input("Enter the name of the website to be blocked from the above list of websites: "))
temp = 0
for i in list_of_websites:

    if i.find(name) != -1 or list_of_websites[i].find(name) != -1:

        host.write("127.0.0.1" + " " + list_of_websites[i] + '\n')

        print("Blocked " + list_of_websites[i])

        temp = 1

if temp == 0:
	
    print ("Couldn't block the website!")
	
host.close()

host.write("127.0.0.1" + "	" + list_of_websites[i] + "\n")