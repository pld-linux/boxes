%define name	boxes
%define version	1.0
%define release	1
%define prefix	/usr
%define cfgfile	%prefix/share/boxes

%define nvr	%{name}-%{version}-%{release}
%define defbr	/var/tmp/%{nvr}-build

name:		%name
version:	%version
release:	%release

vendor:         Thomas Jensen <boxes@home-of.tj>
packager:	Thomas Jensen <boxes@home-of.tj>

summary:	Draw any kind of box around some given text
group:		Utilities/Text

copyright:	GPL Version 2
URL:		http://home.pages.de/~jensen/boxes/

source:		http://home.pages.de/~jensen/boxes/download/%{name}-%{version}-src.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"boxes" can draw all kinds of boxes around its input text, ranging from a C
comment box to complex ASCII art. These boxes may also be removed, even if
they have been badly damaged by editing of the text inside. Since boxes may
be open on any side, "boxes" can also be used to create regional comments in
any programming language. With the help of an editor macro or mapping,
damaged boxes can easily be repaired. New box designs of all sorts can
easily be added and shared by appending to a free format configuration file.

%description -l pl
Za pomoc� boxes mo�na rysowa� r�ne ramki wok� podanego tekstu, pocz�wszy
od komentarzy C a sko�czywszy na skomplikowanym ascii art. Mo�na r�wnie�
usuwa� te ramki, nawet jesli zosta�y powa�nie uszkodzone edycj� znajduj�cego
si� w nich tekstu. Poniewa� mog� by� otwarte z ka�dej strony, mo�na ich
u�y� do tworzenia lokalnych komentarzy w jakimkolwiek j�zyku programowania.
Za pomoc� edytora makr lub mapowania mo�na �atwo naprawi� uszkodzone ramki. 
Mo�na r�wnie� �atwo doda� nowe rodzaje ramek r�nego rodzaju, do��czaj�c je 
do pliku konfiguracyjnego o otwartym formacie.

###########################################################################
# useful macros
###########################################################################
%define cleanroot [ -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" = "%defbuildroot" ] && rm -rf "$RPM_BUILD_ROOT"
%define restorebins [ -f $RPM_BUILD_DIR/$RPM_PACKAGE_NAME.cpio ] && cpio -iv -I $RPM_BUILD_DIR/$RPM_PACKAGE_NAME.cpio
###########################################################################

%prep
%setup

%build
rm doc/boxes.1
rm src/boxes.h
make GLOBALCONF=%cfgfile

%install
mkdir -p $RPM_BUILD_ROOT/%prefix/bin
mkdir -p $RPM_BUILD_ROOT/%prefix/man/man1
mkdir -p $RPM_BUILD_ROOT/%prefix/share

install -m 0755 src/boxes	$RPM_BUILD_ROOT/%prefix/bin
install -m 0644 doc/boxes.1 	$RPM_BUILD_ROOT/%prefix/man/man1
install -m 0644 boxes-config 	$RPM_BUILD_ROOT/%cfgfile

# write filelisting to /tmp
find "$RPM_BUILD_ROOT" -type f -printf "/%P\n" > /tmp/FILES-%nvr

%clean
# delete stuff
[ "$RPM_BUILD_ROOT" = "%defbr" -a -d "%defbr" ] && rm -rf %defbr

%files
%defattr(-, root, root)
/usr/bin/boxes
/usr/man/man1/boxes.1
%config /usr/share/boxes
%doc COPYING README
