import excel_reader
import pexpect
import time
import os

def connect_server():
    excel_rows = excel_reader.read_excel("code.xlsx")
    for excel_row in excel_rows:
        disk_stat(excel_row[1])

def ssh_command(user, host, password, command):
    ssh_new_key = 'Are you sure you want to continue connecting'
    child = pexpect.spawn('ssh -l %s %s %s' % (user, host, command))
    i = child.expect([pexpect.TIMEOUT, ssh_new_key, 'password: '])
    if i == 0:
        print('ERROR!')
        print('SSH could not login. Here is what SSH said:')
        print(child.before, child.after)
        return None
    if i == 1:
        child.sendline('yes')
        child.expect('password: ')
        i = child.expect([pexpect.TIMEOUT, 'password: '])
        if i == 0:
            print('ERROR!')
            print('SSH could not login. Here is what SSH said:')
            print(child.before, child.after)
            return None
    child.sendline(password)
    return child

def disk_stat(server_ip):
    child = ssh_command("root", server_ip, "tu597561694", "df -h")
    child.expect(pexpect.EOF)
    disk = child.before
    disklist = str(disk, encoding='utf-8').strip().split('\n')
    disklists = []
    for disk in disklist:
        disklists.append(disk.strip().split())
    print('************************磁盘空间监控****************************')
    print("*******************时间：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "******************")
    for  i in disklists[1:]:
        print("\t文件系统：", i[0], end = " ")
        print("\t容量：", i[1], end = " ")
        print("\t已用：", i[2], end = "")
        print("\t可用：", i[3], end = " ")
        print("\t已用%挂载点：", i[4])


connect_server()


