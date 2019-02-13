Name:      onemetre-camera-server
Version:   2.2.0
Release:   0
Url:       https://github.com/warwick-one-metre/camd
Summary:   Camera control server for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python36, python36-Pyro4, python36-numpy, python36-astropy
Requires:  python36-warwick-observatory-common, python36-warwick-w1m-camera
Requires:  observatory-log-client, %{?systemd_requires}
# Required for the andor SDK to detect the cameras
Requires: libusb-devel

%description
Part of the observatory software for the Warwick one-meter telescope.

camd interfaces with and wraps the Andor camera and exposes it via Pyro.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/camd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/blue_camd.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/red_camd.service %{buildroot}%{_unitdir}

%post
%systemd_post blue_camd.service
%systemd_post red_camd.service

%preun
%systemd_preun blue_camd.service
%systemd_preun red_camd.service

%postun
%systemd_postun_with_restart blue_camd.service
%systemd_postun_with_restart red_camd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/camd
%defattr(-,root,root,-)
%{_unitdir}/blue_camd.service
%{_unitdir}/red_camd.service

%changelog
