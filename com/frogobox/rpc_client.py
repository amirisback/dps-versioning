# import library xmlrpc client karena akan digunakan rpc
import xmlrpc.client

from com.frogobox.config import *

rpcServer = xmlrpc.client.ServerProxy(BASE_CONFIG_URL)


number1 = 16
number2 = 4

print(str(number1) + " + " + str(number2) + " = " + str(rpcServer.plusMath(number1, number2)))
print(str(number1) + " * " + str(number2) + " = " + str(rpcServer.multipleMath(number1, number2)))
print(str(number1) + " / " + str(number2) + " = " + str(rpcServer.divideMath(number1, number2)))
print(str(number1) + " - " + str(number2) + " = " + str(rpcServer.minusMath(number1, number2)))
print(str(number1) + "pow(" + str(number2) + ") = " + str(rpcServer.powMath(number1, number2)))

# print semua fungsi yang ada di komputer remote
print(rpcServer.system.listMethods())
