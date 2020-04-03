#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xAB4655A126D292E4 (coreteam@netfilter.org)
#
Name     : libnftnl
Version  : 1.1.6
Release  : 19
URL      : http://netfilter.org/projects/libnftnl/files/libnftnl-1.1.6.tar.bz2
Source0  : http://netfilter.org/projects/libnftnl/files/libnftnl-1.1.6.tar.bz2
Source1  : http://netfilter.org/projects/libnftnl/files/libnftnl-1.1.6.tar.bz2.sig
Summary  : Netfilter nf_tables infrastructure library
Group    : Development/Tools
License  : GPL-2.0
Requires: libnftnl-lib = %{version}-%{release}
Requires: libnftnl-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32libmnl)
BuildRequires : pkgconfig(libmnl)

%description
No detailed description available

%package dev
Summary: dev components for the libnftnl package.
Group: Development
Requires: libnftnl-lib = %{version}-%{release}
Provides: libnftnl-devel = %{version}-%{release}
Requires: libnftnl = %{version}-%{release}
Requires: libnftnl = %{version}-%{release}

%description dev
dev components for the libnftnl package.


%package dev32
Summary: dev32 components for the libnftnl package.
Group: Default
Requires: libnftnl-lib32 = %{version}-%{release}
Requires: libnftnl-dev = %{version}-%{release}

%description dev32
dev32 components for the libnftnl package.


%package lib
Summary: lib components for the libnftnl package.
Group: Libraries
Requires: libnftnl-license = %{version}-%{release}

%description lib
lib components for the libnftnl package.


%package lib32
Summary: lib32 components for the libnftnl package.
Group: Default
Requires: libnftnl-license = %{version}-%{release}

%description lib32
lib32 components for the libnftnl package.


%package license
Summary: license components for the libnftnl package.
Group: Default

%description license
license components for the libnftnl package.


%prep
%setup -q -n libnftnl-1.1.6
cd %{_builddir}/libnftnl-1.1.6
pushd ..
cp -a libnftnl-1.1.6 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585928400
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1585928400
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libnftnl
cp %{_builddir}/libnftnl-1.1.6/COPYING %{buildroot}/usr/share/package-licenses/libnftnl/d6458d52bfead6f1399b865f1aeea0caa639ef6c
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/libnftnl/batch.h
/usr/include/libnftnl/chain.h
/usr/include/libnftnl/common.h
/usr/include/libnftnl/expr.h
/usr/include/libnftnl/flowtable.h
/usr/include/libnftnl/gen.h
/usr/include/libnftnl/object.h
/usr/include/libnftnl/rule.h
/usr/include/libnftnl/ruleset.h
/usr/include/libnftnl/set.h
/usr/include/libnftnl/table.h
/usr/include/libnftnl/trace.h
/usr/include/libnftnl/udata.h
/usr/lib64/libnftnl.so
/usr/lib64/pkgconfig/libnftnl.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libnftnl.so
/usr/lib32/pkgconfig/32libnftnl.pc
/usr/lib32/pkgconfig/libnftnl.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnftnl.so.11
/usr/lib64/libnftnl.so.11.3.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libnftnl.so.11
/usr/lib32/libnftnl.so.11.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libnftnl/d6458d52bfead6f1399b865f1aeea0caa639ef6c
