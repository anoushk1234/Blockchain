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
        print("Bkno\t\t\tsecurity")
        for item in reversed(range(1,len(self.chain))):
         if self.chain[item].prevhash==self.chain[item-1].hash:
            print("%f:\t\t\t%s" % (self.chain[item].index," is secure"))
           # print("Block no:"+str(self.chain[item].index)+" is secure")
         else:
            print("%s:\t\t\t%f" % (self.chain[item].index," insecure"))
        print("---------------------------------------------------------------")

    def newblock(self,blk):
        blk.prevhash=self.latestblock().hash
        blk.hash=blk.creat_hash()
        self.chain.append(blk)

chn=Blockchain()
chn.newblock(Block(1,chn.latestblock().hash,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),{"amt":"500"}))
print("Block No\t\t\tprevhash\t\thash\t\tDate & Time\t\tData")
for item in chn.chain:
    print("%f:\t\t\t%s\t\t%s\t\t%s\t\t%s" % (item.index,item.prevhash,item.hash,item.time,item.data))
    # print("Block number000:"+str(item.index)+"\nPrevious hash:"+str(item.prevhash)+"\nHash:"+str(item.hash)+"\nDate & Time:"+str(item.time)+"\nData:"+str(item.data))
print("---------------------------------------------------------------")
print(chn.valid())