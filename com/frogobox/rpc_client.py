# import library xmlrpc client karena akan digunakan rpc
import xmlrpc.client

# import config file
from com.frogobox.config import *

# buat stub/skeleton (proxy) pada client
rpcServer = xmlrpc.client.ServerProxy(BASE_CONFIG_URL)

# versi dari client
version_client = BASE_VERSION_CLIENT

# Menampilkan Versi Client
print("Version Client \t: " + str(version_client))
print("-- Checking Version From Server --")
print("Version Server \t: " + str(rpcServer.get_version_update()))  # Menampilkan versi server
print()
print("Result : ")

print("----------------------------------")
if rpcServer.updated_version(version_client):  # Checking versi server dan client
    print("Latest Version Apps - No Need Update")
else:
    inputUser = input("Apakah Ingin Memperbarui Version? (Y/N) ")
    if inputUser == 'y':
        # Update versi client
        version_client = rpcServer.get_version_update()
        print("Thanks For Update")
        print("Version Client \t : " + str(version_client))
    elif inputUser == 'n':
        # Tidak mengupdate versi Client
        print("Your version not updated")
        print("Version Client \t : " + str(version_client))
    else:
        print("Updating Error")
print("----------------------------------")
