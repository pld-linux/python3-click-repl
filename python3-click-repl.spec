#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	REPL plugin for Click
Summary(pl.UTF-8):	Wtyczka REPL dla Clicka
Name:		python3-click-repl
Version:	0.4.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/click-repl/
Source0:	https://files.pythonhosted.org/packages/source/c/click-repl/click_repl-%{version}.tar.gz
# Source0-md5:	6bf41793093fe8ae608e30eb2885a868
# sdist ships tests/ without __init__.py, which provides mock_stdin
Source1:	https://raw.githubusercontent.com/click-contrib/click-repl/%{version}/tests/__init__.py?/click-repl-tests-init-%{version}.py
# Source1-md5:	e26547a7e6f42eb34b43d04a7462814d
URL:		https://pypi.org/project/click-repl/
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-click >= 7.0
BuildRequires:	python3-click < 9
BuildRequires:	python3-prompt_toolkit >= 3.0.36
BuildRequires:	python3-pytest >= 7.2.1
BuildRequires:	python3-pytest-cov >= 4.0.0
BuildRequires:	python3-typing_extensions >= 4.7.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.9
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
REPL plugin for Click.

%description -l pl.UTF-8
Wtyczka REPL dla Clicka.

%prep
%setup -q -n click_repl-%{version}

cp -p %{SOURCE1} tests/__init__.py

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
