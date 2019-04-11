Name:           trufont
Version:        0.5.0
Release:        1%{?dist}
Summary:        A streamlined and hackable font editor

License:        Public Domain
URL:            https://trufont.github.io
Source0:        https://github.com/trufont/trufont/releases/download/%{version}/TruFont.zip

ExclusiveArch:      x86_64

%description
A streamlined and hackable font editor.


%install
mkdir -p %{buildroot}/usr/bin
unzip %{SOURCE0} -d %{buildroot}/usr/bin
chmod 755 %{buildroot}/usr/bin/TruFont


%prep


%build


%check


%files
/usr/bin/TruFont


%changelog
* Wed Apr 10 2019 Ellen Marie Dash <me@duckie.co> 0.5.0-1
- Initial release of the package
