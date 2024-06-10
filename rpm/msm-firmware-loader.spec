Name:       msm-firmware-loader
Version:    1.5.0
Release:    0
Summary:    Firmware loader script for Qualcomm devices
License:    MIT
URL:        https://github.com/postmarketOS/msm-firmware-loader 
Source:     %{name}-%{version}.tar.gz

%description
msm-firmware-loader is a script that loads various firmware blobs
from dedicated partitions on Qualcomm devices.

%prep
%setup -q -n %{name}-%{version}/msm-firmware-loader

%install
install -Dm755 msm-firmware-loader.sh -t %{buildroot}%{_sbindir}
install -Dm644 msm-firmware-loader.service -t %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_unitdir}/sysinit.target.wants
ln -s ../msm-firmware-loader.service %{buildroot}%{_unitdir}/sysinit.target.wants/msm-firmware-loader.service

%files
%defattr(-,root,root,-)
%license LICENSE
%{_sbindir}/msm-firmware-loader.sh
%{_unitdir}/msm-firmware-loader.service
%{_unitdir}/sysinit.target.wants/msm-firmware-loader.service
