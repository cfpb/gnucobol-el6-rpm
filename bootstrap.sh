#!/usr/bin/env bash

sudo yum -y groupinstall 'Development Tools'

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

if [ "$SCRIPTPATH" = "/tmp" ] ; then
	SCRIPTPATH=/vagrant
fi

mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS}
ln -sf $SCRIPTPATH/SPECS $HOME/rpmbuild/SPECS
echo '%_topdir '$HOME'/rpmbuild' > $HOME/.rpmmacros

# Install Rust
curl -sSf -O https://static.rust-lang.org/rustup.sh
sh rustup.sh -y -s -- --channel=nightly

# Get XSV source
git clone https://github.com/BurntSushi/xsv
tar -cJvf xsv.tar.xz xsv
cp xsv.tar.xz $HOME/rpmbuild/SOURCES/

# Setup LD_LIBRARY_PATH var
echo "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib/" | sudo tee /etc/profile.d/rust.sh
