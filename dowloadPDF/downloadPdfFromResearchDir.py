import paramiko
from paramiko import SSHException
from argparse import ArgumentParser
from scp import SCPClient, SCPException

#base_dir = '/default/main/forrester/WORKAREA/shared/imported/forresterDotCom/Research/'
base_dir = '/raid/prodfiles/forrester/imported/forresterDotCom/Research/'


def parseArguments():
    parser = ArgumentParser()
    parser.add_argument("--server", "-sv")
    parser.add_argument("--username", "-u")
    parser.add_argument("--password", "-pw")
    return parser.parse_args()


def sshClient(a):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(a.server, username=a.username, password=a.password)
    return ssh


ssh = sshClient(parseArguments())
scp = SCPClient(ssh.get_transport(), sanitize=lambda x: x)
contentIds = 'RES129284,RES154278,RES174669,RES174736,RES174975,RES174981,RES175098,RES175376,RES175370,RES175374,RES175375,RES175377,RES175508,RES175489,RES48053,RES47890,RES48017,RES48096,RES48131,RES48334,RES53726,RES53719,RES53418,RES53682,RES53722,RES176083,RES158943,RES137857,RES55230,RES121950,RES176057,RES175937,RES120267,RES91241,RES53618,RES53723,RES55711,RES53419,RES53678,RES55003,RES53681,RES54872,RES57156,RES174698,RES175072,RES175353,RES175136,RES175335,RES175504,RES175379,RES175406,RES175420,RES175434,RES175494,RES175496,RES175498,RES175491,RES175493,RES175495,RES175492,RES175497,RES175499,RES175501,RES175502,RES175503,RES175487,RES175515,RES175500,RES175505,RES175513,RES58349,RES141606,RES176144,RES176094,RES165205,RES176035,RES53392,RES54567,RES175507,RES174671,RES174904,RES176095,RES175127'\
    .split(",")

for id in contentIds:
    document_id = id[3:]
    print(id + ">>" + document_id)
    try:
        scp.get(base_dir + document_id +'/*.pdf', '')
    except SCPException as e:
        print("Operation error with RES%s: %s" % (document_id, e))
    except SSHException as e:
        print("Operation error with RES%s: %s" % (document_id, e))

scp.close()
ssh.close()
