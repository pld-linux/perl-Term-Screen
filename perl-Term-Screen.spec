
# Conditional build:
%bcond_without	tests	# do perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	Term
%define pnam	Screen
Summary:	Term::Screen -  A Simple all perl Term::Cap based screen positioning module
Name:		perl-Term-Screen
Version:	1.02
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-test.patch
# Source0-md5:	16495a66cf592840716c47898e6a6882
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Term::Screen is a very simple screen positioning module that should work wherever "Term::Cap" does. It is set up for Unix
using stty's but these dependences are isolated by evals in the "new" constructor. Thus you may create a child module
implementing Screen with MS-DOS, ioctl, or other means to get raw and unblocked input. This is not a replacement for
Curses -- it has no memory.  This was written so that it could be easily changed to fit nasty systems, and to be avail-
able first thing.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1 

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:make test}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Term/Screen.pm
%{_mandir}/man3/*
