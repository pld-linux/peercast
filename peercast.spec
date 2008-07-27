Summary:	PeerCast: a peer-to-peer streaming client/server
Summary(pl.UTF-8):	PeerCast: klient/serwer strumieni w systemie peer-to-peer
Name:		peercast
Version:	0.1217
Release:	2
License:	GPL
Group:		Applications/Multimedia
Source0:	http://www.peercast.org/src/%{name}-%{version}-src.tgz
# Source0-md5:	d4881d8f1454311ccca8df20c0c1c305
Patch0:		%{name}-buildfix.patch
Patch1:		%{name}-ini-location.patch
Patch2:		%{name}-amd64.patch
Patch3:		%{name}-makefile.patch
Patch4:		%{name}-paths.patch
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

%description -l pl.UTF-8
PeerCast to prosty darmowy sposób na słuchanie radia i oglądanie
przekazu wideo w Internecie. Używa on technologii P2P dla umożliwienia
każdemu nadawania programu bez kosztów tradycyjnego serwera strumieni.
Oznacza to możliwość słuchania i oglądania stacji zwykle niedostępnych
na stronach komercyjnych.

%prep
%setup -qc
find '(' -name '*.cpp' -o -name '*.h' ')' -print0 | xargs -0 sed -i -e 's,\r$,,'

#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__make} -C ui/linux \
	CC="%{__cc}" \
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
