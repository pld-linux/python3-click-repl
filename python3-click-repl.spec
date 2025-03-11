#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	REPL plugin for Click
Summary(pl.UTF-8):	Wtyczka REPL dla Clicka
Name:		python3-click-repl
Version:	0.3.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/click-repl/
Source0:	https://files.pythonhosted.org/packages/source/c/click-repl/click-repl-%{version}.tar.gz
# Source0-md5:	6f91210a103e1927be0c3fa26f9c4430
URL:		https://pypi.org/project/click-repl/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-click >= 7.0
BuildRequires:	python3-prompt_toolkit >= 3.0.36
BuildRequires:	python3-pytest >= 7.2.1
BuildRequires:	python3-pytest-cov >= 4.0.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
REPL plugin for Click.

%description -l pl.UTF-8
Wtyczka REPL dla Clicka.

%prep
%setup -q -n click-repl-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_cov.plugin \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/click_repl
%{py3_sitescriptdir}/click_repl-%{version}-py*.egg-info
