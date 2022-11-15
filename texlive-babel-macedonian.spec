Name:		texlive-babel-macedonian
Version:	39587
Release:	1
Summary:	Babel module to support Macedonian Cyrillic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-macedonian
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-macedonian.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-macedonian.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-macedonian.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides support for Macedonian documents written
in Cyrillic, in babel.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/babel-macedonian
%{_texmfdistdir}/tex/generic/babel-macedonian
%doc %{_texmfdistdir}/doc/generic/babel-macedonian

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
