import socket
import platform
import psutil
import GPUtil


class pcInformation():
    def __init__(self):
        self.hostname = socket.gethostname()
        self.system = platform.system()
        self.version = platform.version()
        self.compiler = platform.python_compiler()
        self.cpu = platform.processor()

        self.memory_total = psutil.virtual_memory().total/1024**3
        self.ramUsed= psutil.virtual_memory().used/1024**3

        self.disk = psutil.disk_usage('/').total/1024**3
        self.diskUsed= psutil.disk_usage('/').used/1024**3
        self.diskFree= psutil.disk_usage('/').free/1024**3
        self.gpu = GPUtil.getGPUs()


        self.disk_used_percent= (self.diskUsed/self.disk)*100



    def print_info(self):
        print("Hostname: ", self.hostname)
        print("System: ", self.system)
        print("Version: ", self.version)
        print("Compiler: ", self.compiler)
        print("CPU: ", self.cpu)
        print(f"Total RAM: {self.memory_total:.2f} GB")
        print(f"Total Disk: {self.disk:.2f} GB")
        print("")
        print("---GPU---")
        print("")

        if not self.gpu:
            print("No GPU information found! Probably using onboard graphics.")
        else:
            for gpus in self.gpu:
                print(f"GPU Name: {gpus.name}")

        print("")
        print("---RAM & Disk usage---")
        print(f"RAM Used: {self.ramUsed:.2f} GB /",f"{self.memory_total:.2f} GB", f"({(self.ramUsed/self.memory_total)*100:.2f} %)")
        print(f"Disk Used: {self.diskUsed:.2f} GB /",f"{self.disk:.2f} GB", f"({self.disk_used_percent:.2f}%)", f"= Disk free {self.diskFree:.2f} GB")




pc_info = outputPcInformation()
pc_info.print_info()
