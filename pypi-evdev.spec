#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-evdev
Version  : 1.6.0
Release  : 33
URL      : https://files.pythonhosted.org/packages/dd/49/d75ac71f54c6c32ac3c63828541740db74d9c764a82496be97b82314d355/evdev-1.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/dd/49/d75ac71f54c6c32ac3c63828541740db74d9c764a82496be97b82314d355/evdev-1.6.0.tar.gz
Summary  : Bindings to the Linux input handling subsystem
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-evdev-filemap = %{version}-%{release}
Requires: pypi-evdev-lib = %{version}-%{release}
Requires: pypi-evdev-license = %{version}-%{release}
Requires: pypi-evdev-python = %{version}-%{release}
Requires: pypi-evdev-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
*evdev*
-------
This package provides bindings to the generic input event interface in
Linux. The *evdev* interface serves the purpose of passing events
generated in the kernel directly to userspace through character
devices that are typically located in ``/dev/input/``.

%package filemap
Summary: filemap components for the pypi-evdev package.
Group: Default

%description filemap
filemap components for the pypi-evdev package.


%package lib
Summary: lib components for the pypi-evdev package.
Group: Libraries
Requires: pypi-evdev-license = %{version}-%{release}
Requires: pypi-evdev-filemap = %{version}-%{release}

%description lib
lib components for the pypi-evdev package.


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
Requires: pypi-evdev-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(evdev)

%description python3
python3 components for the pypi-evdev package.


%prep
%setup -q -n evdev-1.6.0
cd %{_builddir}/evdev-1.6.0
pushd ..
cp -a evdev-1.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658155283
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
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
cp %{_builddir}/evdev-1.6.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-evdev/4ab6a6236dcbd6da7e9d10d79d9c26d7975d2968
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

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-evdev

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-evdev/4ab6a6236dcbd6da7e9d10d79d9c26d7975d2968

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
