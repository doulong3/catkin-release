%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-catkin
Version:        0.8.7
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS catkin package

License:        BSD
URL:            http://wiki.ros.org/catkin
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       cmake
Requires:       gmock-devel
Requires:       gtest-devel
Requires:       python3-catkin_pkg > 0.4.3
Requires:       python3-empy
Requires:       python3-nose
Requires:       python3-setuptools
BuildRequires:  cmake
BuildRequires:  python3-catkin_pkg > 0.4.3
BuildRequires:  python3-empy
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  python3-setuptools
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Low-level build system macros and infrastructure for ROS.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Tue Jul 14 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.8.7-1
- Autogenerated by Bloom

* Thu May 28 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.8.6-1
- Autogenerated by Bloom

* Thu May 21 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.8.5-1
- Autogenerated by Bloom

* Thu May 14 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.8.4-1
- Autogenerated by Bloom

* Tue Apr 14 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.8.3-1
- Autogenerated by Bloom

* Mon Apr 06 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.8.2-1
- Autogenerated by Bloom

* Mon Mar 02 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.8.1-1
- Autogenerated by Bloom

* Fri Jan 24 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.8.0-1
- Autogenerated by Bloom

* Thu Jan 23 2020 Dirk Thomas <dthomas@osrfoundation.org> - 0.7.21-1
- Autogenerated by Bloom

