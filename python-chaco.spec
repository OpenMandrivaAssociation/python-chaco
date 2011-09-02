%define module	chaco
%define name	python-%{module}
%define version	4.0.1
%define release	%mkrel 1

Summary:	Enthought Tool Suite - chaco project
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://code.enthought.com/projects/chaco/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	python-enthought-chaco
Obsoletes:	python-enthought-chaco2
Requires:	python-traits >= 4.0.0
Requires:	python-enable >= 4.0.0
Requires:	python-numpy >= 1.1.0
Requires:	python-reportlab
BuildRequires:	python-numpy-devel >= 1.1.0
BuildRequires:	python-traits >= 4.0.0
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires: 	python-sphinx

%description
Chaco is a Python plotting application toolkit that facilitates
writing plotting applications at all levels of complexity, from simple
scripts with hard-coded data to large plotting programs with complex
data interrelationships and a multitude of interactive tools. While
Chaco generates attractive static plots for publication and
presentation, it also works well for interactive data visualization
and exploration.

* Flexible drawing and layout: Plots consist of graphical components
  which can be placed inside nestable containers for layout,
  positioning, and event dispatch. Every component has a configurable
  rendering loop with distinct layers and backbuffering. Containers
  can draw cooperatively so that layers span across the containment
  hierarchy.
* Modular and extensible architecture: Chaco is object oriented from
  the ground up for ease of extension and customization. There are
  clear interfaces and abstract classes defining extension points for
  writing your own custom behaviors, from custom tools, plot types,
  layouts, etc. Most classes are also "subclass-friendly", so that
  subclasses can override one or two methods and everything else just
  works.
* Data model for ease of extension and embedding: Chaco separates the
  data from any transformations of the data that are needed for
  displaying it. This separation makes it easier to extend Chaco, or
  embed it in applications.

%prep
%setup -q -n %{module}-%{version}

%build

%__python setup.py build
pushd docs
make html
popd

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt *.rst examples/ docs/*.pdf docs/build/html/
