#
# Conditional build:
%bcond_without	tests	# do perform "make test"

%define		pdir	Term
%define		pnam	Screen
%include	/usr/lib/rpm/macros.perl
Summary:	Term::Screen - a simple all Perl Term::Cap based screen positioning module
Summary(pl.UTF-8):	Term::Screen - prosty perlowy moduł pozycjonowania ekranu oparty na Term::Cap
Name:		perl-Term-Screen
Version:	1.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1a57d3aa267d613a8897933a99f7110e
Patch0:		%{name}-test.patch
URL:		http://search.cpan.org/dist/Term-Screen/
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

%description -l pl.UTF-8
Term::Screen to bardzo prosty moduł do pozycjonowania ekranu, który
powinien działać zawsze kiedy Term::Cap działa. Jest skonfigurowany
dla Uniksów i używania stty, ale te zależności są wydzielone do
instrukcji eval w konstruktorze new. W ten sposób można stworzyć moduł
potomny implementujący Screen dla MS-DOS-a, przy użyciu ioctl-i, albo
w inny sposób uzyskując surowe i nieblokujące wejście. Nie jest to
zamiennik Curses - nie ma pamięci. Został napisany tak, aby mógł być
łatwo dopasowany do paskudnych systemów i być pierwszą dostępną
rzeczą.

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
