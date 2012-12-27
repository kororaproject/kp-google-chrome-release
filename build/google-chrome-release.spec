Name:   google-chrome-release
Version:  1.0
Release:  1%{?dist}
Summary:  Google Chrome repository configuration

Group:  System Environment/Base
License:  BSD
URL:    http://google.com/chrome
Source0:  %{name}-%{version}
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch: noarch

%description
Google Chrome repository configuration.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT/etc/yum.repos.d/

install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/etc/pki/rpm-gpg/RPM-GPG-KEY-google-chrome
/etc/yum.repos.d/google-chrome.repo

%changelog
* Thu Dec 27 2012 Ian Firns <firnsy@kororaproject.org> - 1.1
- Initial package.

* Mon Dec 26 2011 Chris Smart <chris@kororaa.org> - 1.0
- Initial package.
