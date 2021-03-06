Name:           python3-warwick-w1m-camera
Version:        1.1.1
Release:        0
License:        GPL3
Summary:        Common backend code for the Warwick one-metre telescope camera daemon
Url:            https://github.com/warwick-one-metre/camd
BuildArch:      noarch

%description
Part of the observatory software for the Warwick one-meter telescope.

python36-warwick-w1m-camera holds the common camera code.

%prep

rsync -av --exclude=build .. .

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%{python3_sitelib}/*

%changelog
