# gunakan xmlrpc bagian server
# import SimpleXMLRPCServer dan SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# buat kelas requesthandler
from com.frogobox.config import *


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = (BASE_CONFIG_PATH)


rpcServer = SimpleXMLRPCServer((BASE_CONFIG_IP_ADDRESS, BASE_CONFIG_PORT), requestHandler=RequestHandler)
rpcServer.register_introspection_functions()


def plusMath(number1, number2):
    return number1 + number2


def minusMath(number1, number2):
    return number1 - number2


def multipleMath(number1, number2):
    return number1 * number2


def divideMath(number1, number2):
    return number1 / number2


def powMath(number1, number2):
    return pow(number1, number2)


rpcServer.register_function(plusMath, 'plusMath')
rpcServer.register_function(multipleMath, 'multipleMath')
rpcServer.register_function(divideMath, 'divideMath')
rpcServer.register_function(minusMath, 'minusMath')
rpcServer.register_function(powMath, 'powMath')

rpcServer.serve_forever()
