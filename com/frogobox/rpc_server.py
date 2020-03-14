# gunakan xmlrpc bagian server
# import SimpleXMLRPCServer dan SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# buat kelas requesthandler
from com.frogobox.config import *


class RequestHandler(SimpleXMLRPCRequestHandler):
    # batasi pada path /RPC2 saja
    rpc_paths = (BASE_CONFIG_PATH)


# Deklarasi versi server
version_server = BASE_VERSION_SERVER

# Menampilkan versi server
print("Version Server \t: " + str(version_server))

# buat server serta register fungsi register_introspection_functions()
rpcServer = SimpleXMLRPCServer((BASE_CONFIG_IP_ADDRESS, BASE_CONFIG_PORT), requestHandler=RequestHandler)
rpcServer.register_introspection_functions()


# Fungsi untuk mengecek versi
def updated_version(version_client):
    if version_client == version_server:
        return True
    else:
        return False


# Fungsi mengembalikan nilai versi server
def get_version_update():
    return version_server


# Registrasi fungsi
rpcServer.register_function(updated_version, 'updated_version')
rpcServer.register_function(get_version_update, 'get_version_update')

# Jalankan server
rpcServer.serve_forever()
