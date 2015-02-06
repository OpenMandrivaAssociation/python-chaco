%define module	chaco

Summary:	Enthought Tool Suite - interactive 2D plotting

Name:		python-%{module}
Version:	4.4.1
Release:	2
Source0:	http://www.enthought.com/repo/ets/chaco-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
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
%doc *.rst
%{py_platsitedir}/%{module}*
