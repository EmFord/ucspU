import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next_value = None

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:
    
    def __init__(self):
        self.head = None

    def add_on_chain(self, timestamp, data):
        if self.head is None:
            self.head = Block(timestamp=timestamp, data=data, previous_hash=None)
            return
        val = self.head
        while val.next_value:
            val = val.next_value
        val.next_value = Block(timestamp=timestamp, data=data, previous_hash=self.head.hash)

    def show_chain(self):
        list_chain = []
        value = self.head
        while(value):
            list_chain.append(value)
            value = value.next_value
        return list_chain

    

# Test Cases

#1.
chain = BlockChain()
chain.add_on_chain(timestamp="1:00", data=["secret data"])
chain.add_on_chain(timestamp="2:00", data=["super secret data"])
print(len(chain.show_chain())) # 2

#2.
chain = BlockChain()
print(len(chain.show_chain())) # 0

#3. Reuse data
chain = BlockChain()
chain.add_on_chain(timestamp="1:00", data=["secret data"])
chain.add_on_chain(timestamp="2:00", data=["super secret data"])
chain.add_on_chain(timestamp="1:00", data=["secret data"])
chain.add_on_chain(timestamp="2:00", data=["super secret data"])
chain.add_on_chain(timestamp="1:00", data=["secret data"])
chain.add_on_chain(timestamp="2:00", data=["super secret data"])
print(chain.show_chain())
print(len(chain.show_chain())) # 6

#4. None Data
chain = BlockChain()
chain.add_on_chain(timestamp="1:00", data=["secret data"])
chain.add_on_chain(timestamp="2:00", data=["super secret data"])
chain.add_on_chain(timestamp="3:00", data=["sakjslkajsljl"])
chain.add_on_chain(timestamp="2:00", data=None)
print(chain.show_chain())
print(len(chain.show_chain())) # 4





