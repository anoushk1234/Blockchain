import random, string
import datetime
class Block:
    def __init__(self,index=0,prevhash="",time="",data={"0":"genesis"}):
        self.index=index
        self.prevhash=prevhash
        self.time=time
        self.data=data
        self.hash=self.creat_hash()
    
    def creat_hash(self):
     return(''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)))

class Blockchain(Block):
    def __init__(self):
        Block.__init__(self)
        now = datetime.datetime.now()
        self.chain=[Block(0,"0",now.strftime("%Y-%m-%d %H:%M:%S"),0)]

    def latestblock(self):
        return self.chain[len(self.chain)-1]
    
    def valid(self):
        if self.latestblock().hash==self.chain[len(self.chain)-2].hash:
            print(str(self.chain[len(self.chain)-2].index)+" is secure")
        else:
            print("insecure")

    def newblock(self,blk):
        blk.prevhash=self.latestblock().hash
        blk.hash=blk.creat_hash()
        self.chain.append(blk)

chn=Blockchain()
chn.newblock(Block(1,chn.latestblock().hash,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),{"amt":"500"}))
for item in chn.chain:
    print("Block number:"+str(item.index)+"\nPrevious hash:"+str(item.prevhash)+"\nHash:"+str(item.hash)+"\nDate & Time:"+str(item.time)+"\nData:"+str(item.data))
    print(item.valid())