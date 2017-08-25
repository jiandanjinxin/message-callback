python /home/limbo/code/py/recv.py
cp /home/limbo/code/py/*.JPG /home/limbo/code/py/test.jpg
rm -rf /home/limbo/code/py/download
sshpass -p passward ssh user@IP rm remotetest/test.jpg
sshpass -p passward scp -6 /home/limbo/code/py/test.jpg limbo@ip:/home/limbo/remotetest/
sshpass -p passward ssh user@ip sh remotetest/remote.sh

sshpass -p passward scp -r -6 user@ip:/home/limbo/remotetest/download /home/limbo/code/py/


python /home/limbo/code/py/sendemail.py
