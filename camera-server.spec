Name:      onemetre-camera-server
Version:   1.8
Release:   0
Url:       https://github.com/warwick-one-metre/camd
Summary:   Camera control server for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-pyds9, python3-numpy, python3-astropy, python3-warwickobservatory, onemetre-obslog-client, %{?systemd_requires}
BuildRequires: systemd-rpm-macros

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
%service_add_pre blue_camd.service
%service_add_pre red_camd.service

%post
%service_add_post blue_camd.service
%service_add_post red_camd.service

%preun
%stop_on_removal blue_camd.service
%stop_on_removal red_camd.service
%service_del_preun blue_camd.service
%service_del_preun redcamd.service

%postun
%restart_on_update blue_camd.service
%restart_on_update red_camd.service
%service_del_postun blue_camd.service
%service_del_postun red_camd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/camd
%defattr(-,root,root,-)
%{_unitdir}/blue_camd.service
%{_unitdir}/red_camd.service

%changelog
