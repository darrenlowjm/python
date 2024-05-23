import shcore
import pytest

from shcore.mc import UseConnection, OutputFormat
from testlib.cli_verify import verifyDiskGroup
from testlib.cli_utils import clearConfig, hasLinear, hasPaged, hasSpear
from testlib.errors import ERROR_RESERVED_NAME_A_OR_B, ERROR_INVALID_SPEAR_RAID_LEVEL, ERROR_INVALID_PARAM, ERROR_MISSING_PARAM, ERROR_VDG_RAID_PARAM
from testlib.get_available_disks import getAvailableDisks, getFormattedDisks
from testlib.mc_factory import MCFactory

# Setup some variables before the testing starts.
_hasLinear = hasLinear()
_hasPaged = hasPaged()
_hasSpear = hasSpear()

def setup_module():
    clearConfig()

def teardown_module():
    clearConfig()
    


def test_linear_dg_with_min_params():
    if not _hasLinear:
        pytest.skip("Must be able to provision linear storage")

    mc = MCFactory(ip=shcore.mcIP)
    with UseConnection(mc.api(), OutputFormat.json) as api:
        dgName = "myLinearGroup1"
        storageType = "Linear"
        level = "RAID5"
        numDisks = 3
        diskStr = getFormattedDisks(connection=api, raid_level=level, num_disks=numDisks)

        api.log("Add a linear disk-group {}.".format(dgName))
        api.checkCmd("add disk-group", dgName, type=storageType, disks=diskStr, level=level)

        verifyDiskGroup(api, dgName, storage_type=storageType, raidtype=level, diskcount=numDisks, chunksize="512k")

        #api.log("Remove the disk-group {}.".format(dgName))
        #api.checkCmd("remove disk-groups", dgName)


@pytest.mark.skip
def test_linear_dg_with_multiple_params():
    if not _hasLinear:
        pytest.skip("Must be able to provision linear storage")

    mc = MCFactory(ip=shcore.mcIP)
    with UseConnection(mc.api(), OutputFormat.json) as api:
        dgName = "myLinearGroup2"
        storageType = "Linear"
        level = "RAID6"
        numDisks = 6
        assignedTo = "B"
        chunkSize = "64k"
        disks = getAvailableDisks(connection=api, num_disks=numDisks)
        numSpares = 2
        numDisks -= numSpares

        api.log("Add a linear disk-group {} with spares, chunk-size, and assign-to.".format(dgName))
        api.checkCmd("add disk-group", dgName, type=storageType, disks=','.join(disks[numSpares:]), level=level, spare=','.join(disks[:numSpares]), assignedTo=assignedTo, chunkSize=chunkSize)

        verifyDiskGroup(api, dgName, storage_type=storageType, raidtype=level, diskcount=numDisks, sparecount=numSpares, owner=assignedTo, chunksize=chunkSize)

        api.log("Remove the disk-group {}.".format(dgName))
        api.checkCmd("remove disk-groups", dgName)
