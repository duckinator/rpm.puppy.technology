%global commit 8f2af5b228366f2b5f4bce982a92f38e74b4b0cd
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate 20181109

%global libdxfrw_commit 03fa5f30f1a1db7231a25653c9dd38044fe06640
%global libdxfrw_shortcommit %(c=%{libdxfrw_commit}; echo ${c:0:7})

Name    : solvespace
Version : 3.0
Release : 1.%{gitdate}git%{shortcommit}%{?dist}
Summary : Parametric 2d/3d CAD
License : GPLv3
URL     : https://github.com/solvespace/solvespace
Source0 : https://github.com/solvespace/solvespace/tarball/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source1 : https://github.com/solvespace/libdxfrw/tarball/%{libdxfrw_commit}/libdxfrw-%{libdxfrw_shortcommit}.tar.gz

BuildRequires : gcc
BuildRequires : gcc-c++
BuildRequires : cmake
BuildRequires : mesa-libGL-devel
BuildRequires : mesa-libGLU-devel
BuildRequires : libspnav-devel
BuildRequires : pkgconfig(zlib)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(fontconfig)
BuildRequires : pkgconfig(glew)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(json-c)
BuildRequires : pkgconfig(gtkmm-3.0)
BuildRequires : pangomm-devel
BuildRequires : pkgconfig(x11)
BuildRequires : desktop-file-utils
Requires : hicolor-icon-theme

# solvespace uses its own forked version of libdxfrw
Provides : bundled(libdxfrw) = 0.6.3

%description
SolveSpace is a parametric 2d/3d CAD program. Applications include modeling
2d and 3d parts, 3d-printed parts, preparing CAM data, mechanism design and
plane and solid geometry.

%package -n libslvs
Summary: SolveSpace geometric kernel

%description -n libslvs
SolveSpace is a parametric 2d/3d CAD proram. libslvs cotains the geometric
kernel of SolveSpace built as a library.

%package -n libslvs-devel
Summary: Development files for SolveSpace geometric kernel
Requires: libslvs%{?_isa} = %{version}-%{release}

%description -n libslvs-devel
SolveSpace is a parametric 2d/3d CAD program. libslvs contains the development
files for the library version of the SolveSpace geometric kernel.

%prep
%autosetup -n solvespace-%{name}-%{shortcommit} -a 1
sed -ie '/^include(GetGitCommitHash)/d' CMakeLists.txt
# libdxfrw git submodule is not included in the tarball, insert manually
rmdir extlib/libdxfrw
mv solvespace-libdxfrw-%{libdxfrw_shortcommit} extlib/libdxfrw

%build
mkdir build
cd build
%cmake .. -DGIT_COMMIT_HASH=%{commit} -DCMAKE_BUILD_TYPE=Release
%make_build

%install
cd build
%make_install

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post -n libslvs -p /sbin/ldconfig

%postun -n libslvs -p /sbin/ldconfig

%files
%{_bindir}/solvespace
%{_bindir}/solvespace-cli
%{_datarootdir}/mime/packages/solvespace-slvs.xml
%{_datarootdir}/solvespace/
%{_datarootdir}/applications/solvespace.desktop
%{_datarootdir}/icons/hicolor/16x16/apps/solvespace.png
%{_datarootdir}/icons/hicolor/24x24/apps/solvespace.png
%{_datarootdir}/icons/hicolor/32x32/apps/solvespace.png
%{_datarootdir}/icons/hicolor/48x48/apps/solvespace.png
%{_datarootdir}/icons/hicolor/16x16/mimetypes/application.x-solvespace.png
%{_datarootdir}/icons/hicolor/24x24/mimetypes/application.x-solvespace.png
%{_datarootdir}/icons/hicolor/32x32/mimetypes/application.x-solvespace.png
%{_datarootdir}/icons/hicolor/48x48/mimetypes/application.x-solvespace.png
%{_datarootdir}/pixmaps/*
%license COPYING.txt
%doc README.md CHANGELOG.md

%files -n libslvs
%{_libdir}/libslvs.so.*
%license COPYING.txt

%files -n libslvs-devel
%{_libdir}/libslvs.so
%{_includedir}/slvs.h

%changelog
* Thu Jan 10 2019 Tavy - 3.0-1.20181109git8f2af5b
- update to more recent solvespace

* Sun May 13 2018 Dominik Schubert - 2.3-3.20170416gitb1d87bf
- Rebuild for Fedora 28
- Remove obsolete scriptlets

* Sun Jan 21 2018 Dominik Schubert - 2.3-2.20170416gitb1d87bf
- Fix dependency on hicolor-icon-theme (should be runtime not build)

* Fri Jan 12 2018 Dominik Schubert - 2.3-1.20170416gitb1d87bf
- Initial packaging

