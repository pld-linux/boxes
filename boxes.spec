Summary:	Draw any kind of box around some given text
Summary(pl.UTF-8):	Rysowanie dowolnych ramek wokół podanego tekstu
Name:		boxes
Version:	2.3.1
Release:	1
License:	GPL v3
Group:		Applications/Text
Source0:	https://github.com/ascii-boxes/boxes/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ff64e5a75018ce337da5fa9a78414152
Patch0:		%{name}-no-strip.patch
URL:		https://boxes.thomasjensen.com/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libunistring-devel
BuildRequires:	ncurses-devel
BuildRequires:	pcre2-32-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"boxes" can draw all kinds of boxes around its input text, ranging
from a C comment box to complex ASCII art. These boxes may also be
removed, even if they have been badly damaged by editing of the text
inside. Since boxes may be open on any side, "boxes" can also be used
to create regional comments in any programming language. With the help
of an editor macro or mapping, damaged boxes can easily be repaired.
New box designs of all sorts can easily be added and shared by
appending to a free format configuration file.

%description -l pl.UTF-8
Za pomocą boxes można rysować różne ramki wokół podanego tekstu,
począwszy od komentarzy C a skończywszy na skomplikowanym ascii art.
Można również usuwać te ramki, nawet jeśli zostały poważnie uszkodzone
edycją znajdującego się w nich tekstu. Ponieważ mogą być otwarte z
każdej strony, można ich użyć do tworzenia lokalnych komentarzy w
jakimkolwiek języku programowania. Za pomocą edytora makr lub
mapowania można łatwo naprawić uszkodzone ramki. Można również łatwo
dodać nowe rodzaje ramek różnego rodzaju, dołączając je do pliku
konfiguracyjnego o otwartym formacie.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS_ADDTL="%{rpmcflags} %{rpmcppflags}" \
	LDFLAGS_ADDTL="%{rpmldflags}" \
	GLOBALCONF="%{_sysconfdir}/boxes.conf"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install -p out/boxes $RPM_BUILD_ROOT%{_bindir}/boxes
cp -p doc/boxes.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -p boxes-config $RPM_BUILD_ROOT%{_sysconfdir}/boxes.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%attr(755,root,root) %{_bindir}/boxes
%{_mandir}/man1/boxes.1*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/boxes.conf
