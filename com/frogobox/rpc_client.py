# import library xmlrpc client karena akan digunakan rpc
import xmlrpc.client

from com.frogobox.config import *

rpcServer = xmlrpc.client.ServerProxy(BASE_CONFIG_URL)

version_client = BASE_VERSION_CLIENT

print("Version Client \t: " + str(version_client))
print("-------------------------")
print()
print("Checking Version....")
print()
print("Version Server \t: " + str(rpcServer.get_version_update()))

if rpcServer.updated_version(version_client):
    print("Latest Version Apps - No Need Update")
else:
    inputUser = input("Apakah Ingin Memperbarui Version? (Y/N) ")
    if inputUser == 'y':
        version_client = rpcServer.get_version_update()
        print("Thanks For Update")
        print("Version Client \t : " + str(version_client))
    elif inputUser == 'n':
        print("Your version not updated")
        print("Version Client \t : " + str(version_client))
    else:
        print("Error")
