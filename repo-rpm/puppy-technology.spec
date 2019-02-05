Name:           puppy-technology
Version:        1.0
Release:        1%{?dist}
Summary:        Enable the puppy.technology repository

License:        Public Domain
URL:            https://github.com/duckinator/rpm.puppy.technology
Source0:        files

BuildArch:      noarch

%description
Adds various files needed by the puppy.technology repository.


%install
mkdir -p %{buildroot}/etc/yum.repos.d/
install -p %{SOURCE0}/etc/yum.repos.d/puppy-technology.repo %{buildroot}/etc/yum.repos.d/


%prep


%build


%check


%files
%license
%doc
/etc/yum.repos.d/puppy-technology.repo


%changelog
* Tue Feb 05 2019 Ellen Marie Dash <me@duckie.co> 1.0-1
- Initial release of the package
