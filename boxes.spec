Summary:	Draw any kind of box around some given text
Summary(pl):	Rysowanie dowolnych ramek wokó³ podanego tekstu
Name:		boxes
Version:	1.0
Release:	1
License:	GPL
Group:		Applications/Text
Vendor:		Thomas Jensen <boxes@home-of.tj>
Source0:	http://boxes.thomasjensen.com/download/%{name}-%{version}.src.tar.gz
# Source0-md5:	fce851c773342ea80cb746ca917448e5
URL:		http://boxes.thomasjensen.com/
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

%description -l pl
Za pomoc± boxes mo¿na rysowaæ ró¿ne ramki wokó³ podanego tekstu,
pocz±wszy od komentarzy C a skoñczywszy na skomplikowanym ascii art.
Mo¿na równie¿ usuwaæ te ramki, nawet je¶li zosta³y powa¿nie uszkodzone
edycj± znajduj±cego siê w nich tekstu. Poniewa¿ mog± byæ otwarte z
ka¿dej strony, mo¿na ich u¿yæ do tworzenia lokalnych komentarzy w
jakimkolwiek jêzyku programowania. Za pomoc± edytora makr lub
mapowania mo¿na ³atwo naprawiæ uszkodzone ramki. Mo¿na równie¿ ³atwo
dodaæ nowe rodzaje ramek ró¿nego rodzaju, do³±czaj±c je do pliku
konfiguracyjnego o otwartym formacie.

%prep
%setup -q

%build
rm -f doc/boxes.1
rm -f src/boxes.h
%{__make} GLOBALCONF="%{_sysconfdir}/boxes.conf"

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
%attr(755,root,root) %{_bindir}/boxes
%{_mandir}/man1/boxes.1
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/boxes.conf
