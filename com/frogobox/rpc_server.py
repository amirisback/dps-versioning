# gunakan xmlrpc bagian server
# import SimpleXMLRPCServer dan SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# buat kelas requesthandler
from com.frogobox.config import *


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = (BASE_CONFIG_PATH)


version_server = BASE_VERSION_SERVER

print(vers)

rpcServer = SimpleXMLRPCServer((BASE_CONFIG_IP_ADDRESS, BASE_CONFIG_PORT), requestHandler=RequestHandler)
rpcServer.register_introspection_functions()


def updated_version(version_client):
    if version_client == version_server:
        return True
    else:
        return False


def get_version_update():
    return version_server


rpcServer.register_function(updated_version, 'updated_version')
rpcServer.register_function(get_version_update, 'get_version_update')

rpcServer.serve_forever()
