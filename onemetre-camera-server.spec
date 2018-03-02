Name:      onemetre-camera-server
Version:   2.1.1
Release:   0
Url:       https://github.com/warwick-one-metre/camd
Summary:   Camera control server for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

# Required for the andor SDK to detect the cameras
Requires: libusb-devel

%if 0%{?suse_version}
Requires:  python3, python34-Pyro4, python34-numpy, python34-astropy, python34-warwick-observatory-common, python34-warwick-w1m-camera, observatory-log-client, %{?systemd_requires}
BuildRequires: systemd-rpm-macros
%endif
%if 0%{?centos_ver}
Requires:  python34, python34-Pyro4, python34-numpy, python34-astropy, python34-warwick-observatory-common, python34-warwick-w1m-camera, observatory-log-client, %{?systemd_requires}
%endif

%description
Part of the observatory software for the Warwick one-meter telescope.

camd interfaces with and wraps the Andor camera and exposes it via Pyro.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/camd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/blue_camd.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/red_camd.service %{buildroot}%{_unitdir}

%pre
%if 0%{?suse_version}
%service_add_pre blue_camd.service
%service_add_pre red_camd.service
%endif

%post
%if 0%{?suse_version}
%service_add_post blue_camd.service
%service_add_post red_camd.service
%endif
%if 0%{?centos_ver}
%systemd_post blue_camd.service
%systemd_post red_camd.service
%endif

%preun
%if 0%{?suse_version}
%stop_on_removal blue_camd.service
%service_del_preun blue_camd.service
%stop_on_removal red_camd.service
%service_del_preun red_camd.service
%endif
%if 0%{?centos_ver}
%systemd_preun blue_camd.service
%systemd_preun red_camd.service
%endif

%postun
%if 0%{?suse_version}
%restart_on_update blue_camd.service
%service_del_postun blue_camd.service
%restart_on_update red_camd.service
%service_del_postun red_camd.service
%endif
%if 0%{?centos_ver}
%systemd_postun_with_restart blue_camd.service
%systemd_postun_with_restart red_camd.service
%endif

%files
%defattr(0755,root,root,-)
%{_bindir}/camd
%defattr(-,root,root,-)
%{_unitdir}/blue_camd.service
%{_unitdir}/red_camd.service

%changelog
