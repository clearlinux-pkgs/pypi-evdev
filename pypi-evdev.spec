#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-evdev
Version  : 1.6.1
Release  : 40
URL      : https://files.pythonhosted.org/packages/05/50/629b011a7f61cb2fca754ea8631575784bf8605a1ec4d6970a010bc54e2b/evdev-1.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/05/50/629b011a7f61cb2fca754ea8631575784bf8605a1ec4d6970a010bc54e2b/evdev-1.6.1.tar.gz
Summary  : Bindings to the Linux input handling subsystem
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-evdev-license = %{version}-%{release}
Requires: pypi-evdev-python = %{version}-%{release}
Requires: pypi-evdev-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
*evdev*
-------
This package provides bindings to the generic input event interface in
Linux. The *evdev* interface serves the purpose of passing events
generated in the kernel directly to userspace through character
devices that are typically located in ``/dev/input/``.

%package license
Summary: license components for the pypi-evdev package.
Group: Default

%description license
license components for the pypi-evdev package.


%package python
Summary: python components for the pypi-evdev package.
Group: Default
Requires: pypi-evdev-python3 = %{version}-%{release}

%description python
python components for the pypi-evdev package.


%package python3
Summary: python3 components for the pypi-evdev package.
Group: Default
Requires: python3-core
Provides: pypi(evdev)

%description python3
python3 components for the pypi-evdev package.


%prep
%setup -q -n evdev-1.6.1
cd %{_builddir}/evdev-1.6.1
pushd ..
cp -a evdev-1.6.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685560278
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-evdev
cp %{_builddir}/evdev-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-evdev/acf705de0f303598fa3aa882cb57a0ee67e98a17 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-evdev/acf705de0f303598fa3aa882cb57a0ee67e98a17

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
