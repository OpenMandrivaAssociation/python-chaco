%define module	chaco
%define name	python-%{module}
%define version	4.2.0
%define	rel		1
%if %mdkversion < 201100
%define release	%mkrel %{rel}
%else
%define	release %{rel}
%endif

Summary:	Enthought Tool Suite - interactive 2D plotting
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/chaco/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	python-enthought-chaco
Obsoletes:	python-enthought-chaco2
Requires:	python-traits >= 4.2.0
Requires:	python-enable >= 4.2.0
Requires:	python-numpy >= 1.1.0
Requires:	python-reportlab
BuildRequires:	python-numpy-devel >= 1.1.0
BuildRequires:	python-traits >= 4.2.0
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	x11-server-xvfb, procps
BuildRequires:	python-setupdocs >= 1.0.5
BuildRequires:	python-sphinx

%description
Chaco is a Python plotting application toolkit that facilitates
writing plotting applications at all levels of complexity, from simple
scripts with hard-coded data to large plotting programs with complex
data interrelationships and a multitude of interactive tools. While
Chaco generates attractive static plots for publication and
presentation, it also works well for interactive data visualization
and exploration.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build
Xvfb :100 -ac &
XPID=$!
export DISPLAY=:100.0
%__python setup.py build_docs
kill -9 $XPID

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt *.rst examples/ docs/*.pdf build/docs/html/
%py_platsitedir/%{module}*
