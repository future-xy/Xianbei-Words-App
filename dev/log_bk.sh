#!/bin/sh

touch /root/DatabaseProject_server/app.log

source /etc/profile
echo 'This is the log' | mail -s 'Log' -a /root/DatabaseProject_server/app.log database_app@sina.com                             

datename=$(date +%Y-%m-%d-%H-%M-%S)
mv /root/DatabaseProject_server/app.log /root/DatabaseProject_server/backuplog/$datename.log.bk
find /root/DatabaseProject_server/backuplog -mtime +30 -name "*.log.bk" -exec rm -f {} \;