#!/usr/bin/env bash

sudo yum -y groupinstall 'Development Tools'
sudo yum -y install gmp gmp-devel db4 db4-devel ncurses ncurses-devel

SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

if [ "$SCRIPTPATH" = "/tmp" ] ; then
	SCRIPTPATH=/vagrant
fi

mkdir -p $HOME/rpmbuild/{BUILD,RPMS,SOURCES,SRPMS}
ln -sf $SCRIPTPATH/SPECS $HOME/rpmbuild/SPECS
echo '%_topdir '$HOME'/rpmbuild' > $HOME/.rpmmacros

# Get GnuCOBOL source
wget http://downloads.sourceforge.net/project/open-cobol/gnu-cobol/1.1/gnu-cobol-1.1.tar.gz -P $HOME/rpmbuild/SOURCES/ -q
