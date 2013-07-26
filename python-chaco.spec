%define module	chaco

Summary:	Enthought Tool Suite - interactive 2D plotting
Name:		python-%{module}
Version:	4.3.0
Release:	1
Source0:	https://www.enthought.com/repo/ets/chaco-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/chaco/
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
BuildRequires:	pkgconfig(lapack)

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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%files
%doc *.txt *.rst examples/ docs/*.pdf build/docs/html/
%py_platsitedir/%{module}*


%changelog
* Mon Aug 13 2012 Lev Givon <lev@mandriva.org> 4.2.0-1
+ Revision: 814714
- Update to 4.2.0.

* Tue Dec 27 2011 Lev Givon <lev@mandriva.org> 4.1.0-1
+ Revision: 745667
- Update to 4.1.0.

* Fri Sep 02 2011 Lev Givon <lev@mandriva.org> 4.0.1-1
+ Revision: 697901
- Update to 4.0.1.

* Thu Jul 07 2011 Lev Givon <lev@mandriva.org> 4.0.0-1
+ Revision: 689214
- import python-chaco



