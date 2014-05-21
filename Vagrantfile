# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # Build master & minion from Vagrant's precise64 image
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"
  config.vm.synced_folder "salt-state-tree/", "/srv/salt"
  
  # Use the host machine's resolver as a DNS proxy
  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--memory", "512"]
  end

  # Master config options
  config.vm.define :master do |master|

    master.vm.provision :salt do |s|
      s.master_config = "master-config"
      s.verbose = true
      # s.run_highstate = true
      s.install_master = true

      # Install from the 2014.1 branch
      s.install_type = "git"
      s.install_args = "2014.1"
    end
    master.vm.hostname = "master"
    master.vm.network :private_network, ip: "192.168.12.13"
  end

  # Minion config options
  config.vm.define :minion do |minion|

    minion.vm.network :private_network, ip: "192.168.12.14"
    minion.vm.provision :salt do |s|
      s.minion_config = "minion-config"
      s.verbose = true
      s.run_highstate = true

      # Install from the 2014.1 branch
      s.install_type = "git"
      s.install_args = "2014.1"
    end
    minion.vm.hostname = "minion"
  end

end
