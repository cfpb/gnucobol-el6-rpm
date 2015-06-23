gnucobol-el6-rpm
================

Description
-----------

RPM build of GNUCobol

Build Instructions
------------------

Ensure that you have Vagrant installed with a virtual machine provider like Virtualbox

1. Clone the repo, and cd into the new directory
2. Run `vagrant up`, which executes the boostrap.sh setup script
3. Run `vagrant ssh` to connect to the newly created VM
4. Run `rpmbuild -ba rpmbuild/SPECS/gnucobol.spec`

To install the newly created RPM pacakge

1. sudo yum install rpmbuild/RPMS/x86_64/gnucobol-1.1-1.x86_64.rpm
