############################
# Set global SPEC variables
############################
%global prefix /usr/local
%global bindir %{prefix}/bin

###############
# Set metadata
###############
Name: xsv
Version: 0.9.3
Release: 1
Summary: a command line program for indexing, slicing, analyzing, splitting and joining CSV files
Group: Applications/File
License: MIT
URL: https://github.com/BurntSushi/xsv
Source: xsv.tar.xz
Obsoletes: xsv <= 0.9.3
Provides: xsv = 0.9.3

%description
xsv is a command line program for indexing, slicing, analyzing, splitting and joining CSV files. Commands should be simple, fast and composable:

1. Simple tasks should be easy.
2. Performance trade offs should be exposed in the CLI interface.
3. Composition should not come at the expense of performance.


########################################################
# PREP and SETUP
# The prep directive removes existing build directory
# and extracts source code so we have a fresh
# code base.
########################################################
%prep
%setup -n xsv

###########################################################
# BUILD
# The build directive does initial prep for building,
# then runs the configure script and then make to compile.
# Compiled code is placed in %{buildroot}
###########################################################
%build
cargo build --release

###########################################################
# INSTALL
# This directive is where the code is actually installed
# in the %{buildroot} folder in preparation for packaging.
###########################################################
%install
mkdir -p %{buildroot}%{bindir}/
cp -p target/release/xsv %{buildroot}%{bindir}/

###########################################################
# CLEAN
# This directive is for cleaning up post packaging, simply
# removes the buildroot directory in this case.
###########################################################
%clean
# Sanity check before removal of old buildroot files
[ -d "%{buildroot}" -a "%{buildroot}" != "/" ] && rm -rf %{buildroot}


##############################################################
# FILES
# The files directive must list all files that were installed
# so that they can be included in the package.
##############################################################
%files
%defattr(-,root,root,-)
%{bindir}/*

# This directive is for changes made post release.
%changelog
