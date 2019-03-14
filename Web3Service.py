from web3 import Web3
from web3.eth import Eth
import os


class Web3Service:
    
    def __init__(self, http_endpoint):
        self.w3 = Web3(Web3.HTTPProvider(http_endpoint))
        self.eth = Eth(self.w3)
        # self.accountPK = os.environ.get('PK')
        self.accountPBK = self.w3.toChecksumAddress("0xb7e888BEa1ABAF7e999E8f66Dd826b4d046E40A5")#("0x40A5673B35dbB64CeeF457ba68Eceb29bd3f96Fb")
        print("Started web3 service")

    def sign_tx(self,contractFunc,options=None): # This will generate a signed tx with the private key of the service
        nonce = self.eth.getTransactionCount(self.accountPBK)
        tx = contractFunc.buildTransaction({
            'nonce':nonce,
            'gasPrice': self.w3.toWei('21', 'gwei')
        })
        pk = os.environ.get('PK')
        signedTx = self.eth.account.signTransaction(tx,private_key=pk)
        return signedTx
