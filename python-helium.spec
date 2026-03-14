Name:		python-helium
Version:	7.0.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/h/helium/helium-%{version}.tar.gz
Summary:	Lighter browser automation based on Selenium.
URL:		https://pypi.org/project/helium/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Lighter browser automation based on Selenium.

%files
%{py_sitedir}/helium
%{py_sitedir}/helium-*.*-info
