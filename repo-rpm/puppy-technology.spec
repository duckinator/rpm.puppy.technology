Name:           puppy-technology
Version:        1
Release:        1%{?dist}
Summary:        Enable the puppy.technology repository.

License:        Public Domain
URL:            https://github.com/duckinator/rpm.puppy.technology
Source0:        files

%description
Adds various files needed by the puppy.technology repository.


%install
mkdir -p %{buildroot}/etc/yum.repos.d/
install -p -m 755 %{SOURCE0}/etc/yum.repos.d/puppy-technology.repo %{buildroot}/etc/yum.repos.d/


%check


%files
%license
%doc


%changelog

