# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

bootstrap_script = <<BOOTSTRAP
#!/bin/bash
set -ex
LOGFILE=/var/log/bootstrap
log () { tee -a ${LOGFILE} ; }
echo "$(date) - Starting bootstrap script" | log
apt-get update | log
apt-get install -y python3 python3-pip | log
pip3 install -r /vagrant/requirements.txt | log
echo "$(date) - Installed packages" | log
mkdir -p /var/lib/cicada/jobs/test
cp /vagrant/example_job_file.json /var/lib/cicada/jobs/test/config.json
screen -d -m python3 /vagrant/cicadad.py
BOOTSTRAP

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/xenial64"

  config.vm.provider "virtualbox" do |virtualbox|
    virtualbox.memory = 512
    virtualbox.cpus = 1
  end

  config.vm.provision "shell", inline: bootstrap_script

  config.vm.network :forwarded_port, guest: 5000, host:5000

end
