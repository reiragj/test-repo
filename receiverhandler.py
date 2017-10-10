import subprocess
import os
import csv

class controller:
    
    def __init__(self):
        self.result = []
        self.thread = []
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.processid = 0
        self.listname = "\processlist.csv"
        self.plist = self.get_process_list()
        
        

    def results(self):
        for line in self.result:
            print line
        return

    def get_process_id(self):
        return self.processid

    def set_process_id(self,processid):
        self.processid = processid
        return

    def del_process_id(self, filename):
        del self.plist[filename]
        self.update_process_list()
        return
        

    def get_process_list(self):
        plist = {}
        try:
            f = open(self.path + self.listname , 'rb')
        except IOError as e:
            print(str(e))
        else:
            reader = csv.reader(f)
            plist = dict(reader)            
        return plist

    def get_list(self):
        return self.plist

    def set_process_list(self, pid, filename):
        self.plist[filename] = pid
        return    

    def update_process_list(self):
        with open(self.path + self.listname, 'wb') as f:
            writer = csv.writer(f)
            for key, value in self.plist.items():
                writer.writerow([key, value])
        f.close()
        return

    def run_process(self, filename):
        _filename = [filename]
        _flag = self.val_process(filename)

        if(_flag):
            return "The process is already running!!"
        else:
            print"running..."
            process = subprocess.Popen(["Python","test.py"]+_filename,
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE )
            #process = subprocess.Popen(['python /opt/pyrobotarm/test.py %s' %filename],shell = True)
            #print(process.stdout)
            #print(process.stderr)
            self.set_process_list(process.pid, filename)
            self.update_process_list()
            
        
        return _flag
    
    def kill_process(self, filename):
        if (self.val_process(filename) == 0):
            print "Not defined thread!"
        else:
            try:
                killprocess = subprocess.Popen('taskkill /F /PID {0}'.format(self.processid), shell=True,
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE)
				#os.killpg(os.getpgid(int(self.proessid)), signal.SIGTERM)
            except:                
                print "Killing error!"
                pass
            else:
                print(killprocess.stderr)
                print "Process killing is done!"
                self.del_process_id(filename)            
        return

    def val_process(self, filename):
        flag = 0
        if(filename in self.plist):
            self.processid=self.plist.get(filename)
            flag = 1        
        return flag

    def Check_Process(self):
        return
   

if __name__ == "__main__":
        print("excuted")
        test = controller()
        print test.run_process("test15.txt")
        #test.val_process("test16.txt")
        #test.killProcess(pid)
        #print(test.get_process_list())
        #test.killProcess("test1.txt")
        print test.plist
else:
        print("Hello, Crypto power is awesome")

    
