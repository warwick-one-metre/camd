Name:      onemetre-camera-client
Version:   1.7
Release:   0
Url:       https://github.com/warwick-one-metre/camd
Summary:   Camera control client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwickobservatory

%description
Part of the observatory software for the Warwick one-meter telescope.

cam is a commandline utility for controlling the red and blue cameras.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/cam %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/cam %{buildroot}/etc/bash_completion.d/cam

%files
%defattr(0755,root,root,-)
%{_bindir}/cam
/etc/bash_completion.d/cam

%changelog
