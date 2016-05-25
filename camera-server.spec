Name:      onemetre-{CAMERA}-camera-server
Version:   1.4
Release:   0
Url:       https://github.com/warwick-one-metre/camd
Summary:   Camera control server for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-pyds9, python3-numpy, python3-astropy, %{?systemd_requires}
BuildRequires: systemd-rpm-macros

%description
Part of the observatory software for the Warwick one-meter telescope.

{CAMERA}d interfaces with and wraps the Andor camera and exposes it via Pyro.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/{CAMERA}d %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/{CAMERA}d.service %{buildroot}%{_unitdir}

%pre
%service_add_pre {CAMERA}d.service

%post
%service_add_post {CAMERA}d.service
%fillup_and_insserv -f -y {CAMERA}d.service

%preun
%stop_on_removal {CAMERA}d.service
%service_del_preun {CAMERA}d.service

%postun
%restart_on_update {CAMERA}d.service
%service_del_postun {CAMERA}d.service

%files
%defattr(0755,root,root,-)
%{_bindir}/{CAMERA}d
%defattr(-,root,root,-)
%{_unitdir}/{CAMERA}d.service

%changelog
