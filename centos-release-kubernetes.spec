%global KubernetesVersion 19

Summary: Kubernetes from the CentOS Virt SIG
Name: centos-release-kubernetes%{KubernetesVersion}
Version: 1.0
Release: 1%{?dist}
License: GPL
URL: https://wiki.centos.org/SpecialInterestGroup/Virtualization

Source0: CentOS-Kubernetes.repo
Source1: RPM-GPG-KEY-CentOS-SIG-Virtualization

%description
yum configuration for Kubernetes packages from the CentOS Virt SIG.

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Kubernetes-%{KubernetesVersion}.repo
sed -i -e "s/KUB_VERSION/%{KubernetesVersion}/g" %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Kubernetes-%{KubernetesVersion}.repo
install -p -d %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Kubernetes-%{KubernetesVersion}.repo
%{_sysconfdir}/pki/rpm-gpg

%changelog
* Fri Feb 16 2018 Spyros Trigazis <spyridon.trigazis@cern.ch>
- Initial version
