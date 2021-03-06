Name:   google-chrome-release
Version:  1.2
Release:  3%{?dist}
Summary:  Google Chrome repository configuration

Group:  System Environment/Base
License:  BSD
URL:    http://google.com/chrome
Source0:  %{name}-%{version}.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch: noarch

%description
Google Chrome repository configuration.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/etc/default
install -m 644 google-chrome $RPM_BUILD_ROOT/etc/default/

install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 google-chrome.repo $RPM_BUILD_ROOT/etc/yum.repos.d/

install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 RPM-GPG-KEY-google-chrome $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/etc/pki/rpm-gpg/RPM-GPG-KEY-google-chrome
/etc/default/google-chrome
%config(noreplace) /etc/yum.repos.d/google-chrome.repo

%changelog
* Wed Aug 12 2015 Chris Smart <csmart@kororaproject.org> - 1.2-3
- Fix content of google-chrome config to prevent overwriting of repo config. Thanks to @jeka on GitHub.

* Sat Jul 25 2015 Ian Firns <firnsy@kororaproject.org> - 1.2-2
- Don't let chrome do it's own repo management, that's our job.

* Sat Aug 17 2013 Chris Smart <csmart@kororaproject.org> - 1.1-2
- Exclude beta and unstable packages by default, leaving only stable.

* Thu Dec 27 2012 Ian Firns <firnsy@kororaproject.org> - 1.1-1
- Initial package.

* Mon Dec 26 2011 Chris Smart <chris@kororaa.org> - 1.0-1
- Initial package.
