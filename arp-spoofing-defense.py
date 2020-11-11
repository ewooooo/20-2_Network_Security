class ArpEntry():
    def __init__(self, line):
        self.ip, self.hw_type, self.flags, self.hw_address, self.mask, self.device = line.split()
    

class Spoofing_Defense():
    def __init__(self):
        self.entries = []

    def loop(self):
        
        lines = open('/proc/net/arp').readlines()[1:]
        for line in lines:
            self.entries.append(ArpEntry(line))

        # 중복확인
        count={}
        for i in self.entries:
            try: 
                count[i.hw_address] += 1
                if count.get(i.hw_address) > 1:
                    print("warning spoofing 발생")
            except: count[i.hw_address]=1


if __name__ == "__main__":
    sd = Spoofing_Defense()
    sd.loop()