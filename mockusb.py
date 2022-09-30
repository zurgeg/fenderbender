# Mock USB emulator
# Intended only for testing.

class USBDev:
  def __init__(self, devid, name, port):
    self.devid = devid
    self.name = name
    self.port = port
  def send(self, packet):
    print(f"{self.name} ({self.devid}) on {self.port.pid}> {hex(packet)}")
  def recv(self, amount):
    print(f"{self.port.num}< {hex(self.port.recv(amount)}")

