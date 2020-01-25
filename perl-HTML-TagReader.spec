#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	HTML
%define		pnam	TagReader
Summary:	HTML::TagReader - reading HTML/SGML/XML files by tags
Summary(pl.UTF-8):	HTML::TagReader - czytanie plików HTML/SGML/XML po znaczniku
Name:		perl-HTML-TagReader
Version:	1.10
Release:	12
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a8e725be2877306454aecf31132cee08
URL:		http://search.cpan.org/dist/HTML-TagReader/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
# for tr_imgaddsize
Requires:	perl-Image-Size >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The module implements a fast and small object oriented way of
processing any kind of HTML/SGML/XML files by tag.

The getbytoken(0) is similar to while(<>) but instead of reading lines
it reads tags or tags and text.

HTML::TagReader makes it easy to keep track of the line number in a
file even though you are not reading the file by line. This important
if you want to implement error messages about HTML errors in your
code.

%description -l pl.UTF-8
Ten moduł implementuje szybką, obiektowo zorientowaną metodę
przetwarzania dowolnego rodzaju plików HTML/SGML/XML po znaczniku.

getbytoken(0) jest podobne do while(<>), ale zamiast czytania linii
czyta znaczniki lub znaczniki i tekst.

HTML::TagReader umożliwia łatwe śledzenie numeru linii w pliku nawet
jeśli nie jest on czytany po linii. Jest to ważne przy implementowaniu
komunikatów błędów dotyczących HTML-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/tr_*
%{perl_vendorarch}/HTML/TagReader.pm
%dir %{perl_vendorarch}/auto/HTML/TagReader
%attr(755,root,root) %{perl_vendorarch}/auto/HTML/TagReader/TagReader.so
%{_mandir}/man[13]/*
