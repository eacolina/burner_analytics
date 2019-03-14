from Web3Service import Web3Service
from TransactionCount import TXCounter

if __name__ == "__main__":
    w3service = Web3Service('https://dai.poa.network')
    txCounter = TXCounter(w3service)
    txCounter.getTxByGasPrice(21000000000)