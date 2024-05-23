
    #========================================
    #'show system'
    #========================================
if 1:
    data = {'system':   [{'object-name': 'system-information', 'meta': '/meta/system', 'system-name': 'Uninitialized Name', 'system-contact': 'Uninitialized   Contact', 'system-location': 'Uninitialized Location', 'system-information': 'Uninitialized Info', 'midplane-serial-number': 'CN0PJ27VFCG0005K01M8A00', 'url': '/system/', 'vendor-name': 'Quantum', 'product-id': 'QXS', 'product-brand': 'Q-Series', 'scsi-vendor-id': 'Quantum', 'scsi-product-id': 'QXS', 'enclosure-count': 2, 'health': 'OK', 'health-numeric': 0, 'health-reason': '', 'other-MC-status': 'Operational', 'other-MC-status-numeric': 3, 'pfuStatus': 'Idle', 'pfuStatus-numeric': 0, 'supported-locales': 'English (English), German (Deutsch), Spanish (español), French (français), Italian (italiano), Japanese (日本語), Korean (한국어), Dutch (Nederlands), Chinese-Simplified (简体中文), Chinese-Traditional (繁體中文)', 'current-node-wwn': 'N/A', 'fde-security-status': 'Unsecured', 'fde-security-status-numeric': 1, 'platform-type': 'Indium', 'platform-type-numeric': 6, 'platform-brand': 'Unknown', 'platform-brand-numeric': 16,                       
    'redundancy': [{'object-name': 'system-redundancy', 'meta': '/meta/redundancy', 'redundancy-mode': 'Active-Active ULP', 'redundancy-mode-numeric': 8, 
                                        'redundancy-status': 'Redundant', 'redundancy-status-numeric': 2, 'controller-a-status': 'Operational', 'controller-a-status-numeric': 0, 'controller-a-serial-number': 'DHSILCO-2046546216', 'controller-b-status': 'Operational', 'controller-b-status-numeric': 0, 'controller-b-serial-number': 'DHSILCO-2046546223', 'other-MC-status': 'Operational', 'other-MC-status-numeric': 3, 'system-ready': 'Ready', 'system-ready-numeric': 0, 'local-ready': 'Ready', 'local-ready-numeric': 0, 'local-reason': '', 'other-ready': 'Ready', 'other-ready-numeric': 0, 'other-reason': ''
                                        }]
                        }
                 ], 
         'status':   [{'object-name': 'status', 'meta': '/meta/status', 'response-type': 'Success', 'response-type-numeric': 0, 'response': 'Command completed successfully. (2021-08-29 03:29:49)','return-code': 1, 'component-id': '', 'time-stamp': '2021-08-29 03:29:49', 'time-stamp-numeric': 1630207789
                         }
                      ]
        }

if 1:
    data = {    'status': {'ret-code':1 },
                'data'  : {'retdata':2,
                           'retdoc':{'name':'peter',
                                     'addr':{'place':158}   ,
                                     'male': True
                                    }    ,   
                            'retlist':[
                                { 'obj name': [ dict(a=1),dict(a=2) ] },
                                { 'obj name':[ dict(a=3),dict(a=4) ] },
                                { 'obj name':[ dict(a=5),dict(a=6) ] }
                            
                            ]
                            },
                'val'   : 'some value is here'
                }
if 0:
    data = {    'status': {'ret-code':1 },
                'data'  : {'retdata':2,
                           'retdoc':{'name':'peter',
                                     'addr':{'place':158}   ,
                                     'male': True
                                    }    ,   
                            'retlist':[
                                { 'obj name': 1 },
                                { 'obj name':2 },
                                { 'obj name':3 }
                            
                            ]
                            },
                'val'   : 'some value is here'
                }
                
if 0:                
    # ========================================
    # show disks
    # ========================================
    data = {'drives': [
        {'object-name': 'drive', 'meta': '/meta/drives', 'durable-id': 'disk_01.01', 'enclosure-id': 1, 'drawer-id': 0, 'slot': 1, 'location': '1.1', 'url': '/drives/1.1', 'port': 0, 'scsi-id': 0, 'blocksize': 512, 'blocks': 585937500, 'serial-number': '6XN81EV20000M5245ZCU', 'vendor': 'SEAGATE', 'model': 'ST9300653SS', 'revision': '0005', 'secondary-channel': 0, 'container-index': 0, 'member-index': 0, 'description': 'SAS', 'description-numeric': 4, 'architecture': 'HDD', 'architecture-numeric': 1, 'interface': 'SAS', 'interface-numeric': 0, 'single-ported': 'Disabled', 'single-ported-numeric': 0, 'type': 'SAS', 'type-numeric': 4, 'usage': 'AVAIL', 'usage-numeric': 0, 'job-running': '', 'job-running-numeric': 0, 'state': 'AVAIL', 'current-job-completion': '', 'blink': 0, 'locator-led': 'Off', 'locator-led-numeric': 0, 'speed': 0, 'smart': 'Enabled', 'smart-numeric': 1, 'dual-port': 1, 'error': 0, 'fc-p1-channel': 0, 'fc-p1-device-id': 0, 'fc-p1-node-wwn': '5000C5007F1C9FBB', 'fc-p1-port-wwn': '0000000000000000', 'fc-p1-unit-number': 0, 'fc-p2-channel': 0, 'fc-p2-device-id': 0, 'fc-p2-node-wwn': '', 'fc-p2-port-wwn': '', 'fc-p2-unit-number': 0, 'drive-down-code': 0, 'owner': 'A', 'owner-numeric': 1, 'index': 0, 'rpm': 15, 'size': '300.0GB', 'size-numeric': 585937500, 'sector-format': '512n', 'sector-format-numeric': 0, 'transfer-rate': '6.0', 'transfer-rate-numeric': 3, 'attributes': ' ', 'attributes-numeric': 2, 'enclosure-wwn': '500C0FF01E0E513C', 'enclosures-url': '/enclosures/1', 'status': 'Up', 'recon-state': 'N/A', 'recon-state-numeric': 0, 'copyback-state': 'N/A', 'copyback-state-numeric': 0, 'virtual-disk-serial': '', 'disk-group': '', 'storage-pool-name': '', 'storage-tier': 'Standard', 'storage-tier-numeric': 2, 'ssd-life-left': 'N/A', 'ssd-life-left-numeric': 255, 'led-status': ' Online', 'led-status-numeric': 0, 'disk-dsd-count': 1, 'spun-down': 0, 'number-of-ios': 0, 'total-data-transferred': '0B', 'total-data-transferred-numeric': 0, 'avg-rsp-time': 0, 'fde-state': 'Not FDE Capable', 'fde-state-numeric': 1, 'lock-key-id': '00000000', 'import-lock-key-id': '00000000', 'fde-config-time': 'N/A', 'fde-config-time-numeric': 0, 'temperature': '33 C', 'temperature-numeric': 33, 'temperature-status': 'OK', 'temperature-status-numeric': 1, 'pi-formatted': 'No', 'pi-formatted-numeric': 0, 'power-on-hours': 52358, 'extended-status': 0, 'health': 'OK', 'health-numeric': 0, 'health-reason': '', 'health-recommendation': ''}, 
        {'object-name': 'drive', 'meta': '/meta/drives', 'durable-id': 'disk_01.02', 'enclosure-id': 1, 'drawer-id': 0,'slot': 2, 'location': '1.2', 'url': '/drives/1.2', 'port': 0, 'scsi-id': 1, 'blocksize': 512, 'blocks': 585937500, 'serial-number': '6XN80GAJ0000N5240WLD', 'vendor': 'SEAGATE', 'model': 'ST9300653SS', 'revision': '0005', 'secondary-channel': 0, 'container-index': 0, 'member-index': 0, 'description': 'SAS', 'description-numeric': 4, 'architecture': 'HDD', 'architecture-numeric': 1, 'interface': 'SAS', 'interface-numeric': 0, 'single-ported': 'Disabled', 'single-ported-numeric': 0, 'type': 'SAS', 'type-numeric': 4, 'usage': 'AVAIL', 'usage-numeric': 0, 'job-running': '', 'job-running-numeric': 0, 'state': 'AVAIL', 'current-job-completion': '', 'blink': 0, 'locator-led': 'Off', 'locator-led-numeric': 0, 'speed': 0, 'smart': 'Enabled', 'smart-numeric': 1, 'dual-port': 1, 'error': 0, 'fc-p1-channel': 0, 'fc-p1-device-id': 1, 'fc-p1-node-wwn': '5000C5007F1F3FEF', 'fc-p1-port-wwn': '0000000000000000', 'fc-p1-unit-number': 0, 'fc-p2-channel': 0, 'fc-p2-device-id': 0, 'fc-p2-node-wwn': '', 'fc-p2-port-wwn': '', 'fc-p2-unit-number': 0, 'drive-down-code': 0, 'owner': 'A', 'owner-numeric': 1, 'index': 1, 'rpm': 15, 'size': '300.0GB', 'size-numeric': 585937500, 'sector-format': '512n', 'sector-format-numeric': 0, 'transfer-rate': '6.0', 'transfer-rate-numeric': 3, 'attributes': ' ', 'attributes-numeric': 2, 'enclosure-wwn': '500C0FF01E0E513C', 'enclosures-url': '/enclosures/1', 'status': 'Up', 'recon-state': 'N/A', 'recon-state-numeric': 0, 'copyback-state': 'N/A', 'copyback-state-numeric': 0, 'virtual-disk-serial': '', 'disk-group': '', 'storage-pool-name': '', 'storage-tier': 'Standard', 'storage-tier-numeric': 2, 'ssd-life-left': 'N/A', 'ssd-life-left-numeric': 255, 'led-status': ' Online', 'led-status-numeric': 0, 'disk-dsd-count': 1, 'spun-down': 0, 'number-of-ios': 0, 'total-data-transferred': '0B', 'total-data-transferred-numeric': 0, 'avg-rsp-time': 0, 'fde-state': 'Not FDE Capable', 'fde-state-numeric': 1, 'lock-key-id': '00000000', 'import-lock-key-id': '00000000', 'fde-config-time': 'N/A', 'fde-config-time-numeric': 0, 'temperature': '34 C', 'temperature-numeric': 34, 'temperature-status': 'OK', 'temperature-status-numeric': 1, 'pi-formatted': 'No', 'pi-formatted-numeric': 0, 'power-on-hours': 52357, 'extended-status': 0, 'health': 'OK', 'health-numeric': 0, 'health-reason': '', 'health-recommendation': ''}, 
        {'object-name': 'drive', 'meta': '/meta/drives', 'durable-id': 'disk_01.04', 'enclosure-id': 1, 'drawer-id': 0, 'slot': 4, 'location': '1.4', 'url': '/drives/1.4', 'port': 0, 'scsi-id': 3, 'blocksize': 512, 'blocks': 585937500, 'serial-number': '6XN7YNHS0000N52154SC', 'vendor': 'SEAGATE', 'model': 'ST9300653SS', 'revision': '0005', 'secondary-channel': 0, 'container-index': 0, 'member-index': 0, 'description': 'SAS', 'description-numeric': 4, 'architecture': 'HDD', 'architecture-numeric': 1, 'interface': 'SAS', 'interface-numeric': 0, 'single-ported': 'Disabled', 'single-ported-numeric': 0, 'type': 'SAS', 'type-numeric': 4, 'usage': 'AVAIL', 'usage-numeric': 0, 'job-running': '', 'job-running-numeric': 0, 'state': 'AVAIL', 'current-job-completion': '', 'blink': 0, 'locator-led': 'Off', 'locator-led-numeric': 0, 'speed': 0, 'smart': 'Enabled', 'smart-numeric': 1, 'dual-port': 1, 'error': 0, 'fc-p1-channel': 0, 'fc-p1-device-id': 3, 'fc-p1-node-wwn': '5000C5007ED9A843', 'fc-p1-port-wwn': '0000000000000000', 'fc-p1-unit-number': 0, 'fc-p2-channel': 0, 'fc-p2-device-id': 0, 'fc-p2-node-wwn': '', 'fc-p2-port-wwn': '', 'fc-p2-unit-number': 0, 'drive-down-code': 0, 'owner': 'A', 'owner-numeric': 1, 'index': 2, 'rpm': 15, 'size': '300.0GB', 'size-numeric': 585937500, 'sector-format': '512n', 'sector-format-numeric': 0, 'transfer-rate': '6.0', 'transfer-rate-numeric': 3, 'attributes': ' ', 'attributes-numeric': 2, 'enclosure-wwn': '500C0FF01E0E513C', 'enclosures-url': '/enclosures/1', 'status': 'Up', 'recon-state': 'N/A', 'recon-state-numeric': 0, 'copyback-state': 'N/A', 'copyback-state-numeric': 0, 'virtual-disk-serial': '','disk-group': '', 'storage-pool-name': '', 'storage-tier': 'Standard', 'storage-tier-numeric': 2, 'ssd-life-left': 'N/A', 'ssd-life-left-numeric': 255, 'led-status': ' Online', 'led-status-numeric': 0, 'disk-dsd-count': 1, 'spun-down': 0, 'number-of-ios': 0, 'total-data-transferred': '0B', 'total-data-transferred-numeric': 0, 'avg-rsp-time': 0, 'fde-state': 'Not FDE Capable', 'fde-state-numeric': 1, 'lock-key-id': '00000000', 'import-lock-key-id': '00000000', 'fde-config-time': 'N/A', 'fde-config-time-numeric': 0, 'temperature': '33 C', 'temperature-numeric': 33, 'temperature-status': 'OK', 'temperature-status-numeric': 1, 'pi-formatted': 'No', 'pi-formatted-numeric': 0, 'power-on-hours': 53439,'extended-status': 4, 'health': 'Degraded', 'health-numeric': 1, 'health-reason': 'The system determined that the indicated disk is degraded because it experienced a number of disk errors in excess of a configured threshold.', 'health-recommendation': 'Monitor the disk.'}], 

        'status': [{'object-name': 'status', 'meta': '/meta/status', 'response-type': 'Success', 'response-type-numeric': 0, 'response': 'Command completed successfully. (2021-09-07 09:07:58)', 'return-code': 0, 'component-id': '', 'time-stamp': '2021-09-07 09:07:58', 'time-stamp-numeric': 1631005678}]
    }
    # ========================================
    # show ports
    # ========================================


    data =  {'port': 
    [{'object-name': 'ports', 'meta': '/meta/port', 'durable-id': 'hostport_A1', 'controller': 'A', 'controller-numeric': 1, 'port': 'A1', 'url': '/ports/A1', 'port-type': 'FC', 'port-type-numeric': 6, 'media': 'FC(-)', 'target-id': '207000c0ff1e0e51', 'status':'Disconnected', 'status-numeric': 6, 'actual-speed': '', 'actual-speed-numeric': 255, 'configured-speed': 'Auto', 'configured-speed-numeric': 3, 'fan-out': 1, 'health': 'Fault', 'health-numeric': 2, 'health-reason': 'An unsupported SFP was detected. The SFP is not compatible with this system. You must use an SFP that is qualified for use in this system.', 'health-recommendation': '- Validate the SFP is supported, and configure the protocol via the set host-port-mode command.', 'fc-port': [{'object-name': 'port-details', 'meta': '/meta/fc-port', 'configured-topology': 'PTP', 'configured-topology-numeric': 1, 'primary-loop-id': 'N/A', 'sfp-status': 'Not compatible', 'sfp-status-numeric': 0, 'sfp-present': 'Present', 'sfp-present-numeric': 1, 'sfp-vendor': 'AVAGO', 'sfp-part-number': 'AFBR-57D7APZ', 'sfp-revision': 'G2.3', 'sfp-supported-speeds': '2G,4G,8G', 'sfp-supported-speeds-numeric': 84}, {'object-name': 'port-details', 'meta': '/meta/fc-port', 'configured-topology': 'PTP', 'configured-topology-numeric': 1, 'primary-loop-id': 'N/A', 'sfp-status': 'Not compatible', 'sfp-status-numeric': 0, 'sfp-present': 'Present', 'sfp-present-numeric': 1, 'sfp-vendor': 'AVAGO', 'sfp-part-number': 'AFBR-57D7APZ', 'sfp-revision': 'G2.3', 'sfp-supported-speeds': '2G,4G,8G', 'sfp-supported-speeds-numeric': 84}, {'object-name': 'port-details', 'meta': '/meta/fc-port', 'configured-topology': 'PTP', 'configured-topology-numeric': 1, 'primary-loop-id': 'N/A', 'sfp-status': 'Not compatible', 'sfp-status-numeric': 0, 'sfp-present': 'Present', 'sfp-present-numeric': 1, 'sfp-vendor': 'AVAGO', 'sfp-part-number': 'AFBR-57D7APZ', 'sfp-revision': 'G2.3', 'sfp-supported-speeds': '2G,4G,8G', 'sfp-supported-speeds-numeric': 84}  ]},    
    {'object-name': 'ports', 'meta': '/meta/port','durable-id': 'hostport_A2', 'controller': 'A', 'controller-numeric': 1, 'port': 'A2', 'url': '/ports/A2', 'port-type': 'FC', 'port-type-numeric': 6, 'media': 'FC(-)', 'target-id': '217000c0ff1e0e51','status': 'Disconnected', 'status-numeric': 6, 'actual-speed': '', 'actual-speed-numeric': 255, 'configured-speed': 'Auto', 'configured-speed-numeric': 3, 'fan-out': 1, 'health': 'N/A', 'health-numeric': 4, 'health-reason': 'There is no active connection to this host port.', 'health-recommendation': '- If this host port is intentionally unused, no action is required.  - Otherwise, use an appropriate interface cable to connect this host port to a switch or host.  - If a cable is connected, check the cable and the switch or host for problems.', 'fc-port': [{'object-name': 'port-details', 'meta': '/meta/fc-port', 'configured-topology': 'PTP', 'configured-topology-numeric': 1, 'primary-loop-id': 'N/A', 'sfp-status': 'Not present', 'sfp-status-numeric': 2, 'sfp-present': 'Not Present', 'sfp-present-numeric': 0, 'sfp-vendor': '', 'sfp-part-number': '', 'sfp-revision': '', 'sfp-supported-speeds': 'N/A', 'sfp-supported-speeds-numeric': 0}]}, 
    {'object-name': 'ports', 'meta': '/meta/port', 'durable-id': 'hostport_B1', 'controller': 'B', 'controller-numeric': 0, 'port': 'B1', 'url': '/ports/B1', 'port-type': 'FC', 'port-type-numeric': 6, 'media': 'FC(-)', 'target-id': '247000c0ff1e0e51', 'status': 'Disconnected', 'status-numeric': 6, 'actual-speed': '', 'actual-speed-numeric': 255, 'configured-speed': 'Auto', 'configured-speed-numeric': 3, 'fan-out': 1, 'health': 'Fault', 'health-numeric': 2, 'health-reason': 'An unsupported SFP was detected. The SFP is not compatible with this system. You must use an SFP that is qualified for use in this system.', 'health-recommendation': '- Validate the SFP is supported, and configure the protocol via the set host-port-mode command.', 'fc-port': [{'object-name': 'port-details', 'meta': '/meta/fc-port', 'configured-topology': 'PTP', 'configured-topology-numeric': 1, 'primary-loop-id': 'N/A', 'sfp-status': 'Not compatible', 'sfp-status-numeric': 0, 'sfp-present': 'Present', 'sfp-present-numeric': 1, 'sfp-vendor': 'AVAGO', 'sfp-part-number': 'AFBR-57D7APZ', 'sfp-revision': 'G2.3', 'sfp-supported-speeds': '2G,4G,8G', 'sfp-supported-speeds-numeric': 84}]}, 
    {'object-name': 'ports', 'meta': '/meta/port', 'durable-id': 'hostport_B2', 'controller': 'B', 'controller-numeric': 0, 'port': 'B2', 'url': '/ports/B2', 'port-type': 'FC', 'port-type-numeric': 6, 'media': 'FC(-)', 'target-id': '257000c0ff1e0e51', 'status': 'Disconnected', 'status-numeric': 6, 'actual-speed': '', 'actual-speed-numeric': 255, 'configured-speed': 'Auto', 'configured-speed-numeric': 3, 'fan-out': 1, 'health': 'N/A', 'health-numeric': 4, 'health-reason': 'There is no active connection to this host port.', 'health-recommendation': '- If this host port is intentionally unused, no action is required.  - Otherwise, use an appropriate interface cable to connect this host port to a switch or host.  - If a cable is connected, check the cable and the switch or host for problems.', 'fc-port': [{'object-name': 'port-details', 'meta': '/meta/fc-port', 'configured-topology': 'PTP', 'configured-topology-numeric': 1, 'primary-loop-id': 'N/A', 'sfp-status': 'Not present', 'sfp-status-numeric': 2, 'sfp-present': 'Not Present', 'sfp-present-numeric': 0, 'sfp-vendor': '', 'sfp-part-number': '', 'sfp-revision': '', 'sfp-supported-speeds': 'N/A', 'sfp-supported-speeds-numeric': 0}]}], 
    'status': [{'object-name': 'status', 'meta': '/meta/status', 'response-type': 'Success', 'response-type-numeric': 0, 'response': 'Command completed successfully. (2021-09-06 17:46:19)', 'return-code': 0, 'component-id': '', 'time-stamp': '2021-09-06 17:46:19', 'time-stamp-numeric': 1630950379}]
    }
                
                

class Response_Json:
    """ doc string
    A class that returns a response object that is able to parse json data
    :param data: json object
    :return: Response object
    """

    def __init__(self, data:dict):
        self.__data = data
        self.__LIST:"internal attribute to indicate a special handling" = False
    
    def json(self) -> dict :
        return list(self.__data.values()) if '_0' in self.__data else self.__data
        
    @property
    def returncode(self) -> str :
        return self.status._0['return-code']
    @property
    def responsetype(self) -> str :
        return self.status._0['response-type']
    @property
    def response_(self) -> str :
        return self.status._0.response
    @property
    def timestamp(self) -> str :
        return self.status._0['time-stamp']

    def __str__(self):
        return str(self.__data)

    def __getitem__(self, item):
        return self.__getattr__(item)
        
    def __getattr__(self, attr):
        print(f'__getattr__ is called with unknown att: {attr}')
        
        if str(attr) == '_LIST':
            self.__LIST = True
            return self

        if self.__LIST:
            print('here')
            #return tuple((value[str(attr)] for value in self.__data.values() ))
            return __class__( { f'_{str(i)}':value[str(attr)] for i,value in enumerate(self.__data.values()) } )

        value = self.__data[str(attr)] 
        #print(f'value={value}')
        
        if isinstance(value, dict):
            return __class__(value)
        elif isinstance(value, list):
            return __class__({ f'_{str(i)}' :j  for i,j in enumerate(value)   })
        else: 
            return value
    
    @classmethod
    def __deconstruct(cls, self):

        pass
        
    def __eq__(self, other:int) -> bool:
        return self.returncode == other
    
    def __bool__(self) -> bool:
        return  self.returncode == 0
        
    def __contains__(self, other:str) -> bool:
        return other.lower() in self.response_.lower()

    def __len__(self) -> int:
        if isinstance(self, __class__): return len(self.json())
        else: return len(obj)
   
        
if 1:        
    a = Response_Json(data)
    






















