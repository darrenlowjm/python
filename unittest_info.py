from information import Show, Data
#import infor
import unittest

# =====================================================================
# test fixture
# =====================================================================
class commandObject_stub    :   
    def showports(self):    
        return  \
        {'port': [{'object-name': 'portsA', 'meta': '/meta/port', 'durable-id': 'hostport_A1', 'controller': 'A', 'controller-numeric': 1, 'fc-port': [{'object-name': 'port-details', 'meta': '/meta/fc-port', 'configured-topology': 'PTP','sfp-supported-speeds-numeric': 84}]},
        {'object-name': 'portsB', 'meta': '/meta/port','durable-id': 'hostport_A2', 'controller': 'A', 'controller-numeric': 1, 'fc-port': [{'object-name': 'port-details', 'meta': '/meta/fc-port', 'configured-topology': 'PTP', 'sfp-supported-speeds-numeric': 0}]} ] }
 
    def showsystem(self):
        return \
            {'system': [
                {'object-name': 'system-information','redundancy': [ {'object-name': 'system-redundancy' }],
                'unhealthy-component': [ {'object-name': 'unhealthy-component'}, {'object-name': 'unhealthy-component'}] 
                }] }    
 
    def showcertificates(self):
        """"""
 
    def showusersmanage(self):
        """"""
 
    def showvolumes(self):
        """"""
 
    def showdisks(self):
        """"""
 
    def showfeatures(self, **kwargs):
        return {'features': [{'object-name': 'features', '32-byte-names': 'Enabled' } ]}

    def showdiskgroups(self, **kwargs):
        return {'disk-groups': [{'object-name': 'disk-group1'},{'object-name': 'disk-group2'} ]}

# =====================================================================
# unit test
# =====================================================================

class unitTest(unittest.TestCase):    
    Show(commandObject_stub)



    def test_features_1(self):
        Show.features()
        self.assertEqual(Data.features.object_name.read(), 'features')
        self.assertEqual(Data.features['32-byte-names'].read(), 'Enabled')
    
    def test_ports_1(self):
        Show.ports()
        self.assertEqual(Data.ports.object_name.read(), ['portsA','portsB'])
        self.assertEqual(Data.ports.object_name.read(), ['portsA','portsB'])
        self.assertEqual(Data.ports.fc_port._ALL.sfp_supported_speeds_numeric.read(), [84,0])
        self.assertEqual(Data.ports.fc_port._ALL.sfp_supported_speeds_numeric.read(), [84,0])
     
    def test_diskgroups_1(self):
        Show.diskgroups()
        self.assertEqual(Data.diskgroups.object_name.read(), ['disk-group1','disk-group2'])
        self.assertEqual(Data.diskgroups.object_name.read(), ['disk-group1','disk-group2'])
        
            
            
        
        
        
            
            
        
        
        
if __name__ == '__main__':
    unittest.main()







