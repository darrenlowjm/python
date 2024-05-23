from shcore import Json_reader, getdisks_utils, getdisks
from shcore.getconfig.getdisks_utils import _SwDisksDict, _SwDict
import pprint
import copy


data = Json_reader(
    {'drives': [
        {'location': '1.0', 'size': '500GB', 'type': 'SAS-MDL', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Performance', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi1', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '1.1', 'size': '500GB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Performance', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '1.2', 'size': '500GB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Performance', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'SED'},
        {'location': '1.3', 'size': '500GB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Performance', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '1.4', 'size': '500GB', 'type': 'SAS+', 'usage': 'NOT AVAIL', 'sector-format': '4K',
         'storage-tier': 'Performance', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '1.5', 'size': '2TB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Performance', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '1.6', 'size': '500GB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Performance', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi1', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '1.7', 'size': '100GB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Performance', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '1.8', 'size': '500GB', 'type': 'SAS-MDL', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Performance', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'SED'},
        {'location': '1.9', 'size': '500GB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Performance', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '1.10', 'size': '1TB', 'type': 'SAS-MDL', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Performance', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi1', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '1.11', 'size': '1TB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Standard', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '1.12', 'size': '1TB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Standard', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'SED'},
        {'location': '1.13', 'size': '1TB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Standard', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '1.14', 'size': '1TB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Standard', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '1.15', 'size': '1TB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Standard', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '1.16', 'size': '1TB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Standard', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi1', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '1.17', 'size': '1TB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Standard', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '1.18', 'size': '1TB', 'type': 'SAS-MDL', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Standard', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'SED'},
        {'location': '1.19', 'size': '500GB', 'type': 'SAS+', 'usage': 'NOT AVAIL', 'sector-format': '4K',
         'storage-tier': 'Standard', 'enclosure-id': 1, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '2.0', 'size': '500GB', 'type': 'SAS-MDL', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Standard', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi1', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '2.1', 'size': '500GB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Standard', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '2.2', 'size': '500GB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Standard', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'SED'},
        {'location': '2.3', 'size': '500GB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Standard', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '2.4', 'size': '500GB', 'type': 'SAS+', 'usage': 'NOT AVAIL', 'sector-format': '4K',
         'storage-tier': 'Standard', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '2.5', 'size': '500GB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '2.6', 'size': '500GB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi1', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '2.7', 'size': '500GB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '2.8', 'size': '500GB', 'type': 'SAS-MDL', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'SED'},
        {'location': '2.9', 'size': '500GB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '2.10', 'size': '1TB', 'type': 'SAS-MDL', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi1', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '2.11', 'size': '1TB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '2.12', 'size': '1TB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'SED'},
        {'location': '2.13', 'size': '1TB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '2.14', 'size': '1TB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '2.15', 'size': '1TB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '2.16', 'size': '1TB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi1', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '2.17', 'size': '1TB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '2.18', 'size': '1TB', 'type': 'SAS-MDL', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'SED'},
        {'location': '2.19', 'size': '1TB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 2, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '3.0', 'size': '500GB', 'type': 'SAS-MDL', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi1', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '3.1', 'size': '500GB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '3.2', 'size': '500GB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'SED'},
        {'location': '3.3', 'size': '500GB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '3.4', 'size': '500GB', 'type': 'SAS+', 'usage': 'NOT AVAIL', 'sector-format': '4K',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '3.5', 'size': '500GB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '3.6', 'size': '500GB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi1', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '3.7', 'size': '500GB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '3.8', 'size': '500GB', 'type': 'SAS-MDL', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'SED'},
        {'location': '3.9', 'size': '500GB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '3.10', 'size': '1TB', 'type': 'SAS-MDL', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi1', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '3.11', 'size': '1TB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '3.12', 'size': '1TB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'SED'},
        {'location': '3.13', 'size': '1TB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'Not Secured'},
        {'location': '3.14', 'size': '1TB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512n',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '3.15', 'size': '1TB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '3.16', 'size': '1TB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi1', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '3.17', 'size': '1TB', 'type': 'SAS', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'FIPS'},
        {'location': '3.18', 'size': '1TB', 'type': 'SAS-MDL', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'SED'},
        {'location': '3.19', 'size': '1TB', 'type': 'SAS+', 'usage': 'AVAIL', 'sector-format': '512e',
         'storage-tier': 'Archive', 'enclosure-id': 3, 'pi-formatted-numeric': 'pi0', 'health': 'OK',
         'fde-state': 'Not Secured'},
    ],
        'status': [
            {'object-name': 'status', 'meta': '/meta/status', 'response-type': 'Success', 'response-type-numeric': 0,
             'response': 'Command completed successfully. (2021-09-07 09:07:58)', 'return-code': 0, 'component-id': '',
             'time-stamp': '2021-09-07 09:07:58', 'time-stamp-numeric': 1631005678}]
    })




'''
disks_dict = _SwDisksDict(
{('SAS+', 'pi0', '512n', '1TB'): {1: ['1.11', '1.12', '1.13', '1.14'], 2: ['2.11', '2.12', '2.13', '2.14'], 3: ['3.11', '3.12', '3.13', '3.14'], 'mixed_output': ['1.11', '1.12', '1.13', '1.14', '2.11', '2.12', '2.13', '2.14', '3.11', '3.12', '3.13', '3.14']}, ('SAS+', 'pi0', '512n', '500GB'): {1: ['1.1', '1.2', '1.3'], 2: ['2.1', '2.2', '2.3'], 3: ['3.1', '3.2', '3.3'], 'mixed_output': ['1.1', '1.2', '1.3', '2.1', '2.2', '2.3', '3.1', '3.2', '3.3']}, ('SAS', 'pi0', '512e', '1TB'): {1: ['1.15', '1.17'], 2: ['2.15', '2.17'], 3: ['3.15', '3.17'], 'mixed_output': ['1.15', '1.17', '2.15', '2.17', '3.15', '3.17']}, ('SAS', 'pi0', '512e', '500GB'): {2: ['2.5', '2.7'], 3: ['3.5', '3.7'], 'mixed_output': ['2.5', '2.7', '3.5', '3.7']}, ('SAS+', 'pi0', '512e', '500GB'): {1: ['1.9'], 2: ['2.9'], 3: ['3.9'], 'mixed_output': ['1.9', '2.9', '3.9']}, ('SAS', 'pi1', '512e', '500GB'): {1: ['1.6'], 2: ['2.6'], 3: ['3.6'], 'mixed_output': ['1.6', '2.6', '3.6']}, ('SAS', 'pi1', '512e', '1TB'): {1: ['1.16'], 2: ['2.16'], 3: ['3.16'], 'mixed_output': ['1.16', '2.16', '3.16']}, ('SAS-MDL', 'pi1', '512n', '500GB'): {1: ['1.0'], 2: ['2.0'], 3: ['3.0'], 'mixed_output': ['1.0', '2.0', '3.0']}, ('SAS-MDL', 'pi1', '512n', '1TB'): {1: ['1.10'], 2: ['2.10'], 3: ['3.10'], 'mixed_output': ['1.10', '2.10', '3.10']}, ('SAS-MDL', 'pi0', '512e', '500GB'): {1: ['1.8'], 2: ['2.8'], 3: ['3.8'], 'mixed_output': ['1.8', '2.8', '3.8']}, ('SAS-MDL', 'pi0', '512e', '1TB'): {1: ['1.18'], 2: ['2.18'], 3: ['3.18'], 'mixed_output': ['1.18', '2.18', '3.18']}, ('SAS+', 'pi0', '512e', '1TB'): {2: ['2.19'], 3: ['3.19'], 'mixed_output': ['2.19', '3.19']}, ('SAS', 'pi0', '512e', '2TB'): {1: ['1.5'], 'mixed_output': ['1.5']}, ('SAS', 'pi0', '512e', '100GB'): {1: ['1.7'], 'mixed_output': ['1.7']}}
).sort_by_least_disks_first()


disks_dict.remove_group_with_less_than_min_disks(sum(num_disk_min)) 
#remove all groups that dont meet min num of mixture requirement
disks_dict.remove_group_with_less_than_min_mixture(len(num_disk_min))
'''

disks_dict = _SwDisksDict({
    'eight':_SwDisksDict({'100':[100.1, 100.2, 100.3], '200':[200.1, 200.2, 200.3, 200.4], '300':[300.1]}), #8 disks
    'seven':_SwDisksDict({'400':[400.1], '600':[600.1, 600.2, 600.3, 600.4], '500':[500.1, 500.2]}),   #7 disks
    'four':_SwDisksDict({'900':[900.1], '800':[800.1, 800.2], '700':[700.1]}),   #4 disks
    'one':_SwDisksDict({'1000':[1000.1]}),   #1 disks
}).sort_by_least_disks_first()

def find_similar_groups_of_disks(disks_dict, disks_list_of_same_group, ordering=None):
    def del_stop_key_and_all_prior_keys_in_dict(dic, stop_key):
        # delete the stop_key as well as all keys prior
        while dic:
            for key in dic.keys():
                del dic[key]
                if key == stop_key:
                    return
                else:
                    break
                    
    # making a copy as we dont want to change the original when we performing the sort
    disks_dict_copy = copy.deepcopy(disks_dict)
    
    #remove all groups that dont meet min requirement
    disks_dict_copy.remove_group_with_less_than_min_disks(sum(disks_list_of_same_group))     
    disks_dict_copy.remove_group_with_less_than_min_mixture(len(disks_list_of_same_group))

    # sort by least num of disks first so that the least disks is picked first
    disks_dict_copy.sort_by_least_disks_first()
        

    pprint.pprint(disks_dict_copy, sort_dicts=False)

    returned_list = list()

    for outer_key, each_mixture_dict in disks_dict_copy.items():
        print(f'*** Starting finding in outer key :{outer_key}')
        
        if ordering == 'DESC':
            each_mixture_dict.sort_dict_by_keys(reverse=True)
        elif ordering == 'ASC':
            each_mixture_dict.sort_dict_by_keys(reverse=False)
        elif ordering is None:
            each_mixture_dict.sort_by_least_disks_first()  
        else:
            raise ValueError(f'Undefined argument for ordering: {ordering}')
        
        for each_num_disk in disks_list_of_same_group:
            #
            #for inner_key, inner_disks_list in each_disk_dict.sort_by_least_disks_first().items():
            for inner_key, inner_disks_list in each_mixture_dict.items():
                if len(inner_disks_list) >= each_num_disk:
                    # found a match                        
                    if ordering is None:
                        # remove this inner_key
                        del each_mixture_dict[inner_key]
                    else:
                        # do this when we dont want to go backwards to check the earlier keys
                        # once we have gone pass it.
                        del_stop_key_and_all_prior_keys_in_dict(each_mixture_dict, inner_key)
                        
                    print(f'* found disk#:{each_num_disk} in \'{outer_key}\': \'{inner_key}\'')
                    returned_list.append((outer_key, inner_key, inner_disks_list))
                    break
            else:
                # cannot find anything in inner dict; break out of disks_list_of_same_group loop!
                print(f'! Cound not find disks#{each_num_disk} in outer key: {outer_key}')
                returned_list = list()
                break           
        else:
            print('ALL found!!')
            break   #out of outer loop
    
    return returned_list

'''
return = [
(common, mixof, list of disk),
,
,
]
'''



if 1:
    num_disk_min = [4, 1]
    disks_dict = data.drives._ALL.get()
    disks_dict = getdisks.common_type_pi_sector_mixof_size_dict(local_data_list=disks_dict)
    ret = find_similar_groups_of_disks(disks_dict, num_disk_min, ordering='ASC')
    print('\nReturned disks:')
    for each in ret:
        print(each)
    
    assert ret == [(('SAS', 'pi0', '512e'), '500GB', ['2.5', '2.7', '3.5', '3.7']),
                   (('SAS', 'pi0', '512e'), '1TB', ['1.15', '1.17', '2.15', '2.17', '3.15', '3.17'])]
                  
                  
    ret = find_similar_groups_of_disks(disks_dict, num_disk_min, ordering='DESC')
    print('\nReturned disks:')
    for each in ret:
        print(each)

    assert ret == [(('SAS', 'pi0', '512e'), '1TB', ['1.15', '1.17', '2.15', '2.17', '3.15', '3.17']),
                   (('SAS', 'pi0', '512e'), '500GB', ['2.5', '2.7', '3.5', '3.7'])]
                
                
    ret = find_similar_groups_of_disks(disks_dict, num_disk_min)
    print('\nReturned disks:')
    for each in ret:
        print(each)

    assert ret == [(('SAS', 'pi0', '512e'), '500GB', ['2.5', '2.7', '3.5', '3.7']),
                   (('SAS', 'pi0', '512e'), '2TB', ['1.5'])]
                  

                  
                  
                  
                  
                  
    print('\n*PASSED')
    
    
    
    
    
    
    
    
    
    
def sort_each_group_by_key_ascending(self, reverse=False):
    """Sort each group of dict by their keys in ascending oder
        Arg: 
            reverse: False(default) means ascending order.
        Example:
            original: 
                {('SAS', 1): {'1TB': ['1.0', '1.1'], '400GB': ['0.3', '0.4']},  # -> notice that '400GB' comes after '1TB'
                 ('SAS+', 0): {'500GB': ['0.1'], '200GB': ['0.3', '0.4'], '800GB': ['0.6']}}
            final after sort:
                {('SAS', 1): {'400GB': ['0.3', '0.4'], '1TB': ['1.0', '1.1']},  # -> notice that '400GB' comes before '1TB'
                 ('SAS+', 0): {'200GB': ['0.3', '0.4'], '500GB': ['0.1'], '800GB': ['0.6']}}        
    """
    if isinstance(self.get_value(0), list):
        # This function is not applicable on list
        raise ValueError('This is a dictionary whose values are list, i.e there is no mixture of disks properties')

    for key in self.data:
        value = self.data[key]
        self.data[key] = value.sort_dict_by_keys(reverse=reverse)    # value is of type _SwDisksDict
    return self

def sort_each_group_by_key_descending(self):
    """Sort each group of dict by their keys in descending oder
        Arg: 
            reverse: True(default) means desending order.
        Example:
            original: 
                {('SAS', 1): {'400GB': ['0.3', '0.4'], '1TB': ['1.0', '1.1']},
                 ('SAS+', 0): {'500GB': ['0.1'], '200GB': ['0.3', '0.4'], '800GB': ['0.6']}}
            final after sort:
                {('SAS', 1): {'1TB': ['1.0', '1.1'], '400GB': ['0.3', '0.4']},
                 ('SAS+', 0): {'800GB': ['0.6']}, '500GB': ['0.1'], '200GB': ['0.3', '0.4']}        
    """
    self.sort_each_group_by_key_ascending(reverse=True)
    return self


