Summary:	Draw any kind of box around some given text
Summary(pl.UTF-8):	Rysowanie dowolnych ramek wokół podanego tekstu
Name:		boxes
Version:	1.1
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://boxes.thomasjensen.com/download/%{name}-%{version}.src.tar.gz
# Source0-md5:	d2ef9fa28a87bf32b3fe0c47ab82fa97
Patch0:		%{name}-cflags.patch
URL:		http://boxes.thomasjensen.com/
BuildRequires:	bison
BuildRequires:	flex
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
%patch0 -p1

%build
rm -f doc/boxes.1
rm -f src/boxes.h
%{__make} \
	CC="%{__cc}" \
	CFLAGS_ADDTL="%{rpmcflags}" \
	GLOBALCONF="%{_sysconfdir}/boxes.conf"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

install src/boxes $RPM_BUILD_ROOT%{_bindir}
install doc/boxes.1 $RPM_BUILD_ROOT%{_mandir}/man1
install boxes-config $RPM_BUILD_ROOT%{_sysconfdir}/boxes.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
