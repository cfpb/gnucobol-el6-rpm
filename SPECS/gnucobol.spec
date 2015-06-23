############################
# Set global SPEC variables
############################
%global prefix /usr/local
%global bindir %{prefix}/bin

###############
# Set metadata
###############
Name: gnucobol
Version: 1.1
Release: 1
Summary: GnuCOBOL is a free COBOL compiler.
Group: Development/Languages
License: GPL 2
URL: http://sourceforge.net/p/open-cobol
Source: gnu-cobol-1.1.tar.gz
Obsoletes: gnucobol <= 0.9.3
Provides: gnucobol = 0.9.3

%description
cobc translates COBOL source code to native executable using intermediate C sources. There is also a version, GnuCOBOL C++, gnu-cobol-cpp, that generates C++ intermediates.
This step in the compile chain, along with the GnuCOBOL dynamic CALL verb implementation, exposes nearly all existing C libraries for direct use by COBOL programmers. (C++ linker for gnu-cobol-cpp).

GnuCOBOL builds executable, shared library, object file and listing from a well integrated cobc command. COBOL and C sources can be mixed in compiler command lines.

GnuCOBOL passes over 9700 of the tests included in the National Institute of Standards and Technology COBOL 85 acceptance test suite.
supports many extensions from other COBOL compilers and adds some nice bits only available with GNU Cobol. FUNCTION SUBSTITUTE being one example of a very useful intrinsic.

While developed to be a useful, production ready COBOL programming tool, GnuCOBOL does NOT claim any level of official COBOL standard support or compliance.

########################################################
# PREP and SETUP
# The prep directive removes existing build directory
# and extracts source code so we have a fresh
# code base.
########################################################
%prep
%setup -n gnu-cobol-1.1 -q

###########################################################
# BUILD
# The build directive does initial prep for building,
# then runs the configure script and then make to compile.
# Compiled code is placed in %{buildroot}
###########################################################
%build
%configure
make

###########################################################
# INSTALL
# This directive is where the code is actually installed
# in the %{buildroot} folder in preparation for packaging.
###########################################################
%install
%make_install

# Remove generated info files
rm -f %{buildroot}/usr/share/info/dir

###########################################################
# CLEAN
# This directive is for cleaning up post packaging, simply
# removes the buildroot directory in this case.
###########################################################
%clean
# Sanity check before removal of old buildroot files
[ -d "%{buildroot}" -a "%{buildroot}" != "/" ] && rm -rf %{buildroot}

###########################################################
# INSTALLATION COMMANDS
###########################################################
%post
/sbin/install-info /usr/share/info/gnu-cobol.info.gz /usr/share/info/dir || :

%preun
/sbin/install-info --delete /usr/share/info/gnu-cobol.info.gz /usr/share/info/dir || :

##############################################################
# FILES
# The files directive must list all files that were installed
# so that they can be included in the package.
##############################################################
%files
%defattr(-,root,root,-)
%{_bindir}/*
/usr/include/*
/usr/lib64/gnu-cobol/*
/usr/lib64/*
/usr/share/gnu-cobol/config/*
/usr/share/gnu-cobol/copy/*
/usr/share/info/gnu-cobol.info.gz
/usr/share/locale/ja/LC_MESSAGES/*

# This directive is for changes made post release.
%changelog
