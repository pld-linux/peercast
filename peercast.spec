Summary:	PeerCast: a peer-to-peer streaming client/server
Summary(pl):	PeerCast: klient/serwer strumieni w systemie peer-to-peer
Name:		peercast
Version:	0.1212
Release:	1
Epoch:		0
License:	GPL
Group:		Applications
# svn://peercast.org/peercast/tags/v%{version}
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	64440769f092fb13ecc79d2097785327
Patch0:		%{name}-buildfix.patch
Patch1:		%{name}-ini-location.patch
URL:		http://www.peercast.org/
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_peercastdir	%{_datadir}/%{name}

%description
PeerCast is a simple, free way to listen to radio and watch video on
the Internet. It uses P2P technology to let anyone become a
broadcaster without the costs of traditional streaming. This means you
get to hear and watch stations not normally found on commercially
funded sites.

%description -l pl
PeerCast to prosty darmowy sposób na s³uchanie radia i ogl±danie
przekazu wideo w Internecie. U¿ywa on technologii P2P dla umo¿liwienia
ka¿demu nadawania programu bez kosztów tradycyjnego serwera strumieni.
Oznacza to mo¿liwo¶æ s³uchania i ogl±dania stacji zwykle niedostêpnych
na stronach komercyjnych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i 's,\./,%{_peercastdir}/,' core/common/peercast.h

%build
%{__make} -C ui/linux \
	CPPFLAGS="%{rpmcxxflags} -D_UNIX" \
	LDFLAGS="%{rpmldflags} -lpthread"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_peercastdir}}
install ui/linux/peercast $RPM_BUILD_ROOT%{_bindir}
cp -r ui/html $RPM_BUILD_ROOT%{_peercastdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_peercastdir}
