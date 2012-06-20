%global modname pyudev

Name:             python-pyudev
Version:          0.15
Release:          1%{?dist}
Summary:          A libudev binding

Group:            Development/Languages
License:          LGPL
URL:              http://pypi.python.org/pypi/pyudev
Source0:          http://pypi.python.org/packages/source/p/pyudev/pyudev-0.15.tar.gz

BuildArch:        noarch


BuildRequires:    python-devel python-setuptools libudev
Requires:         python python-setuptools libudev

%description
###### pyudev ######

pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.

The binding supports CPython_ 2 (2.6 or newer) and 3 (3.1 or newer), and
PyPy_ 1.5 or newer.  It is tested against udev 151 or newer, earlier
versions of udev as found on dated Linux systems may work, but are not
officially supported.

%prep
%setup -q -n %{modname}-%{version}

%build
%{__python} setup.py build 

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc COPYING README.rst
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*


%changelog
* Mon Jun 18 2012 Chris Lockfort <clockfort@redhat.com> 0.15-1
- initial package
