%global srcname emanate

Name:           %{srcname}
Version:        6.0.0
Release:        0%{?dist}
Summary:        Symlinks files from one directory to another, useful for managing dotfiles

License:        MIT
URL:            https://pypi.python.org/pypi/emanate
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel

%{?python_provide:%python_provide python3-%{srcname}}

%description
Symlinks files from one directory to another, similarly to Effuse and Stow.
Useful for managing your dotfiles.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
# We'd normally use `setup.py test`, but for Emanate that's an alias that
# uses dotfiles. And those dotfiles aren't in source distributions.
#%{__python3} setup.py pytest

# Note that there is no %%files section for the unversioned python module
%files
#%license LICENSE.txt
%doc README.md
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/emanate

%changelog
* Sun Mar 17 2019 Ellen Dash - 6.0.0-0
- Update to 6.0.0
- I forgot to add changelog entries for 5.0.x, whoops.

* Wed Mar 06 2019 Ellen Dash - 5.0.0-3
- Initial packaging
