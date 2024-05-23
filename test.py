#from shcore import backoff, sw2_log

class Global_Configuration:
    def __init__(self):
        #
        #self.init()
        self.__flag_initilization_done = False
        self.backoff_pcnt = None

    # --------------------------------
    # public methods
    # --------------------------------
    def init(self):   
        if self.__flag_initilization_done:
            return
            
        self.__set_backoff_to_default()
        self.__flag_initilization_done = True

    def init_by_force(self):
        self.__flag_initilization_done = False
        self.init()
    
    def dump_to_sys_config_file(self):
        SYS_CONFIG_FILE = 'sys_configuration.txt'
        sw2_log.save_file(SYS_CONFIG_FILE, 'hi there!')
    
    # --------------------------------
    # private methods
    # --------------------------------
    def __set_backoff_to_default(self):
        backoff.set_default()
        self.backoff_pcnt = backoff.backoff_pcnt
        
    def __get_advSetting():
        ''''''



global_cfg = Global_Configuration()

