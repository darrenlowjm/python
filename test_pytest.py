import pytest



def skipif_check( *top_args ):
    def inner(func)
        def wrapper(*args, **kwargs): 
            print('I am decorated')
            for each in top_args:
                if not each:
                    pytest.skip('I am skipping due to precondition not met')
            func(*args, **kwargs)               
        return wrapper
    return inner


@inner
def test_comething():
    print('testing done')
    
    
@title('Create Linear Raid 0')
@skipif_check(getFeatures.hasLinear)    
def test_1_01_create_linear_raid0(fixtures_func):

    available_disk_list, available_disk_list_type = get_avail_disks_list(drive_type=True)
    if not getFeatures.hasLinear:
        sw2_log.skip("This system does not support Linear storage.")
    if len(available_disk_list) < MIN_RAID0_DISKS:
        sw2_log.skip(
            f"Not enough drives available. Expected{MIN_RAID0_DISKS} Available{len(available_disk_list)}")

    name = "dgRAID0"

    cmd = {'type':'linear',
           'level': 'RAID0',
           'disks': ','.join(available_disk_list[:MIN_RAID0_DISKS]),
           'returnCode': SUCCESS, }

    sw2_log.info("Create Disk Group {} level RAID0, Expected EC: {}".format(name, cmd['returnCode']))
    raid.create(name, **cmd)

    validation = {'storage-type': 'linear',
                  'raidtype': cmd['level'],
                  'chunksize': '512k',
                  'diskcount': MIN_RAID0_DISKS,
                  'storage-tier': 'N/A',
                  'status': 'UP',
                  }    