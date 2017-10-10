import sys
import logging
import logging.handlers

logger = logging.getLogger('packetlogger')
fomatter = logging.Formatter('%(asctime)s %(filename)s %(message)s')

_DELI = " "
_fileMaxByte = 1024 * 1024 * 100 #100MB
fileHandler = logging.handlers.RotatingFileHandler("/opt/pyrobotarm/" + sys.argv[1], maxBytes=_fileMaxByte, backupCount=10)
fileHandler.setFormatter(fomatter)
logger.addHandler(fileHandler)
logger.setLevel(logging.DEBUG)


def extract_addr(log, addr_index):
    '''Extract to BD Address
       <XXXXX>12345678 ...'''
    return addr[:index];

def extract_data(log, addr_index, axis_len):
    '''Extract to 8-Axis Data'''
    j=addr_index+axis_len
    while(j < 136):
        axis=log[addr_index:j]
        addr_index=j
        j+=axis_len
        parsing_data(axis)
    return;

def parsing_data(log):
    '''Parsing axis_num{2}, run{2}, torque{4}, thermal{4}, status{4}'''
    i = 2
    data = log[:2]+_DELI+log[2:4]
    while(i<5):
        data += " " + hextoint(log[4*(i-1):4*i])
        i += 1
    _logging(data)
    return;

def hextoint(hex):
    return str(int(hex, 16));
        
def _logging(log):
    log = "192.168.0.1"+":"+"5000" + _DELI + log;
	logger.info(log)
	print log
    return  

string = str(timestamp) + _DELI + "192.168.0.1" + _DELI + "5000" + _DELI
log = "d439020100fff0502880000200f123122880000300f2f0502880000400fff2123123000500fff050288001060012f0502880000700ff505028800a0800ff20502812419f"
extract_data(log,6,16) 


