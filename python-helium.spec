%define module helium

Name:		python-helium
Version:	7.0.1
Release:	1
Summary:	Lighter browser automation based on Selenium.
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/helium
Source0:	https://files.pythonhosted.org/packages/source/h/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python

%description
Lighter browser automation based on Selenium.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%license LICENSE.txt
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
