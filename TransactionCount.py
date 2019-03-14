from Web3Service import Web3Service
import csv

class TXCounter:

    def __init__(self, w3service: Web3Service):
        self.web3 = w3service
        csvFile = open('txs_2.csv','w')
        self.csvWriter  = csv.writer(csvFile, delimiter=',')
        
    
    def getTxByGasPrice(self, gasPrice):
        latestBlock = self.web3.eth.getBlock('latest').number
        burnerTxs = []
        for i in range(2191705,latestBlock):
            txs = self.web3.eth.getBlock(i).transactions
            if(len (txs) > 0):
                print(i)
                for j in range(len(txs)):
                    self.csvWriter.writerow(txs[j].hex())
                     
        
        return burnerTxs
    
    def parseBlock(self, transactions, gasPrice):
        selectedTxs = []
        for i in range( len(transactions) ):
            tx = self.web3.eth.getTransaction(transactions[i])
            if(gasPrice == tx.gasPrice):
                selectedTxs.append(tx)
        return selectedTxs