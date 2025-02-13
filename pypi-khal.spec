#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v4
# autospec commit: da8b975
#
Name     : pypi-khal
Version  : 0.11.3
Release  : 74
URL      : https://files.pythonhosted.org/packages/d3/58/665551b1fea58a70d0f70fb539d2cd6be9ec106f36023d62c3ec5c7b2de1/khal-0.11.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/d3/58/665551b1fea58a70d0f70fb539d2cd6be9ec106f36023d62c3ec5c7b2de1/khal-0.11.3.tar.gz
Summary  : A standards based terminal calendar
Group    : Development/Tools
License  : MIT
Requires: pypi-khal-bin = %{version}-%{release}
Requires: pypi-khal-data = %{version}-%{release}
Requires: pypi-khal-license = %{version}-%{release}
Requires: pypi-khal-python = %{version}-%{release}
Requires: pypi-khal-python3 = %{version}-%{release}
Requires: pypi(click_log)
Requires: pypi(urwid)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
khal
====
.. image:: https://github.com/pimutils/khal/actions/workflows/ci.yml/badge.svg?branch=master&event=push
:target: https://github.com/pimutils/khal/actions/workflows/ci.yml

%package bin
Summary: bin components for the pypi-khal package.
Group: Binaries
Requires: pypi-khal-data = %{version}-%{release}
Requires: pypi-khal-license = %{version}-%{release}

%description bin
bin components for the pypi-khal package.


%package data
Summary: data components for the pypi-khal package.
Group: Data

%description data
data components for the pypi-khal package.


%package license
Summary: license components for the pypi-khal package.
Group: Default

%description license
license components for the pypi-khal package.


%package python
Summary: python components for the pypi-khal package.
Group: Default
Requires: pypi-khal-python3 = %{version}-%{release}

%description python
python components for the pypi-khal package.


%package python3
Summary: python3 components for the pypi-khal package.
Group: Default
Requires: python3-core
Provides: pypi(khal)
Requires: pypi(atomicwrites)
Requires: pypi(click)
Requires: pypi(click_log)
Requires: pypi(configobj)
Requires: pypi(icalendar)
Requires: pypi(python_dateutil)
Requires: pypi(pytz)
Requires: pypi(pyxdg)
Requires: pypi(tzlocal)
Requires: pypi(urwid)

%description python3
python3 components for the pypi-khal package.


%prep
%setup -q -n khal-0.11.3
cd %{_builddir}/khal-0.11.3
pushd ..
cp -a khal-0.11.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707768182
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-khal
cp %{_builddir}/khal-%{version}/COPYING %{buildroot}/usr/share/package-licenses/pypi-khal/0b045114e6e06c4f7d3755c79d2b382f3a4b59ee || :
cp %{_builddir}/khal-%{version}/doc/source/license.rst %{buildroot}/usr/share/package-licenses/pypi-khal/e82c6215d146a2f2fbb37ba5515f18c76a051324 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
## install_append content
mkdir -p %{buildroot}/usr/share/defaults/khal/
cp khal.conf.sample %{buildroot}/usr/share/defaults/khal/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ikhal
/usr/bin/khal

%files data
%defattr(-,root,root,-)
/usr/share/defaults/khal/khal.conf.sample

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-khal/0b045114e6e06c4f7d3755c79d2b382f3a4b59ee
/usr/share/package-licenses/pypi-khal/e82c6215d146a2f2fbb37ba5515f18c76a051324

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
