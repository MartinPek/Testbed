sudo chown -v $USER ~/.ssh/known_hosts
ssh-keyscan -H 192.168.1.162 >> ~/.ssh/known_hosts