from abc import ABC, abstractmethod

log_file = "log_file"

class Log(ABC):
    @abstractmethod
    def log(self, msg):
        ...

    def log_error(self, msg):
        print(f"Error: {msg}")

    def log_sucess(self, msg):
        print(f"Sucess: {msg}")    
        
class LogFileMixins(Log):
    def log(self, msg):
        print(msg)
        msg_format = f"{msg}, ({self.__class__.__name__})"
        print("Saving in log", msg_format)
        with open(log_file, "a") as arquivo:
            arquivo.write(msg_format)
            arquivo.write("\n")

class LogPrintMixins(Log):    
    def log(self, msg):
        print(f"{msg}, ({self.__class__.__name__})")

class Eletronic(ABC):
    def __init__(self, name):
        self._name = name
        self._state = False

    def on(self):
        if not self._state:
            self._state = True

    def off(self):
        if not self._state:
            self._state = False

class Smartphone(Eletronic, LogPrintMixins):
    def on(self):
        super().on()

        if self._state:
            msg = f"the {self._name} is on"
            self.log_sucess(msg)
            
    def off(self):
        super().off()

        if not self._state:
            msg = f"the {self._name} is off"    
            self.log_error(msg)

class Pc(Eletronic, LogFileMixins):
    def on(self):
        super().on()

        if self._state:
            msg = f"the {self._name} is on"
            self.log_sucess(msg)
            
    def off(self):
        super().off()

        if not self._state:
            msg = f"the {self._name} is off"    
            self.log_error(msg)


smartphone = Smartphone("Motorola")
pc = Pc("Pichau")

pc.on()
smartphone.off()
pc.on()
smartphone.on()
