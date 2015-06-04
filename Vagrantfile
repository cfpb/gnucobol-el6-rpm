# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  config.vm.box = "chef/centos-6.5"
  config.vm.provision :shell,
    path: "bootstrap.sh",
    privileged: false
end
