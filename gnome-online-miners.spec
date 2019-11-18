Summary:	GNOME Online Miners - crawling through your online contents
Summary(pl.UTF-8):	GNOME Online Miners - indeksowanie własnych treści w sieci
Name:		gnome-online-miners
Version:	3.34.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-online-miners/3.34/%{name}-%{version}.tar.xz
# Source0-md5:	070510f95a8ea5499e9c7e37304abdf9
URL:		https://wiki.gnome.org/Projects/GnomeOnlineMiners
BuildRequires:	gfbgraph-devel >= 0.2.2
BuildRequires:	glib2-devel >= 1:2.35.1
BuildRequires:	gnome-online-accounts-devel >= 3.13.3
BuildRequires:	grilo-devel >= 0.3.0
BuildRequires:	libgdata-devel >= 0.15.2
BuildRequires:	libzapojit-devel >= 0.0.2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker-devel >= 1.0
BuildRequires:	xz
Requires:	gfbgraph >= 0.2.2
Requires:	glib2 >= 1:2.35.1
Requires:	gnome-online-accounts-libs >= 3.13.3
Requires:	grilo >= 0.3.0
Requires:	libgdata >= 0.15.2
Requires:	libzapojit >= 0.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Online Miners provides a set of crawlers that go through your
online content and index them locally in Tracker. It has miners for
Facebook, Flickr, Google, ownCloud and SkyDrive.

%description -l pl.UTF-8
Pakiet GNOME Online Miners zawiera zestaw programów przeszukujących
należące do użytkownika treści w sieci i indeksujące je lokalnie w
Trackerze. Dołączone programy obsługują usługi Facebook, Flickr,
Google, ownCloud oraz SkyDrive.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gnome-online-miners/libgom-1.0.la
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gnome-online-miners

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/gnome-online-miners
%attr(755,root,root) %{_libdir}/gnome-online-miners/libgom-1.0.so
%attr(755,root,root) %{_libexecdir}/gom-facebook-miner
%attr(755,root,root) %{_libexecdir}/gom-flickr-miner
%attr(755,root,root) %{_libexecdir}/gom-gdata-miner
%attr(755,root,root) %{_libexecdir}/gom-media-server-miner
%attr(755,root,root) %{_libexecdir}/gom-owncloud-miner
%attr(755,root,root) %{_libexecdir}/gom-zpj-miner
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Facebook.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Flickr.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.GData.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.MediaServer.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Owncloud.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Zpj.service
