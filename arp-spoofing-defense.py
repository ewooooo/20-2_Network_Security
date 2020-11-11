from psutil import process_iter
from signal import SIGTERM # or SIGKILL

def kill_port():
    print("stop telnet server")
    for proc in process_iter():
        for conns in proc.connections(kind='inet'):
            if conns.laddr.port == 23:
                proc.send_signal(SIGTERM) # or SIGKILL
                continue

class ArpEntry():
    def __init__(self, line):
        self.ip, self.hw_type, self.flags, self.hw_address, self.mask, self.device = line.split()

    def __str__(self):
        return '%s: %s' % (self.ip, self.hw_address)

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
                    print("warning spoofing")
                    print(self.entries)

                    kill_port()
            except: count[i.hw_address]=1


if __name__ == "__main__":
    sd = Spoofing_Defense()
    sd.loop()