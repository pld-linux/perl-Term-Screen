#
# Conditional build:
%bcond_without	tests	# do perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Term
%define	pnam	Screen
Summary:	Term::Screen - a simple all Perl Term::Cap based screen positioning module
Summary(pl):	Term::Screen - prosty perlowy modu³ pozycjonowania ekranu oparty na Term::Cap
Name:		perl-Term-Screen
Version:	1.02
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-test.patch
# Source0-md5:	16495a66cf592840716c47898e6a6882
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Term::Screen is a very simple screen positioning module that should
work wherever "Term::Cap" does. It is set up for Unix using stty's but
these dependences are isolated by evals in the "new" constructor. Thus
you may create a child module implementing Screen with MS-DOS, ioctl,
or other means to get raw and unblocked input. This is not a
replacement for Curses - it has no memory. This was written so that it
could be easily changed to fit nasty systems, and to be available
first thing.

%description -l pl
Term::Screen to bardzo prosty modu³ do pozycjonowania ekranu, który
powinien dzia³aæ zawsze kiedy Term::Cap dzia³a. Jest skonfigurowany
dla uniksów i u¿ywania stty, ale te zale¿no¶ci s± wydzielone do
instrukcji eval w konstruktorze new. W ten sposób mo¿na stworzyæ modu³
potomny implementuj±cy Screen dla MS-DOS-a, przy u¿yciu ioctl-i, albo
w inny sposób uzyskuj±c surowe i nieblokuj±ce wej¶cie. Nie jest to
zamiennik Curses - nie ma pamiêci. Zosta³ napisany tak, aby móg³ byæ
³atwo dopasowany do paskudnych systemów i byæ pierwsz± dostêpn±
rzecz±.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1 

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Term/Screen.pm
%{_mandir}/man3/*
