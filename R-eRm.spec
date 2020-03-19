#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-eRm
Version  : 1.0.1
Release  : 19
URL      : https://cran.r-project.org/src/contrib/eRm_1.0-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/eRm_1.0-1.tar.gz
Summary  : Extended Rasch Modeling
Group    : Development/Tools
License  : GPL-3.0
Requires: R-eRm-lib = %{version}-%{release}
Requires: R-colorspace
Requires: R-psych
BuildRequires : R-colorspace
BuildRequires : R-psych
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-eRm package.
Group: Libraries

%description lib
lib components for the R-eRm package.


%prep
%setup -q -c -n eRm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583274312

%install
export SOURCE_DATE_EPOCH=1583274312
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library eRm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library eRm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library eRm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc eRm || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/eRm/CITATION
/usr/lib64/R/library/eRm/DESCRIPTION
/usr/lib64/R/library/eRm/INDEX
/usr/lib64/R/library/eRm/Meta/Rd.rds
/usr/lib64/R/library/eRm/Meta/data.rds
/usr/lib64/R/library/eRm/Meta/features.rds
/usr/lib64/R/library/eRm/Meta/hsearch.rds
/usr/lib64/R/library/eRm/Meta/links.rds
/usr/lib64/R/library/eRm/Meta/nsInfo.rds
/usr/lib64/R/library/eRm/Meta/package.rds
/usr/lib64/R/library/eRm/Meta/vignette.rds
/usr/lib64/R/library/eRm/NAMESPACE
/usr/lib64/R/library/eRm/NEWS.Rd
/usr/lib64/R/library/eRm/NEWS.pdf
/usr/lib64/R/library/eRm/NEWSRd2txt.R
/usr/lib64/R/library/eRm/R/eRm
/usr/lib64/R/library/eRm/R/eRm.rdb
/usr/lib64/R/library/eRm/R/eRm.rdx
/usr/lib64/R/library/eRm/data/Rdata.rdb
/usr/lib64/R/library/eRm/data/Rdata.rds
/usr/lib64/R/library/eRm/data/Rdata.rdx
/usr/lib64/R/library/eRm/doc/eRm.R
/usr/lib64/R/library/eRm/doc/eRm.Rnw
/usr/lib64/R/library/eRm/doc/eRm.pdf
/usr/lib64/R/library/eRm/doc/index.html
/usr/lib64/R/library/eRm/help/AnIndex
/usr/lib64/R/library/eRm/help/aliases.rds
/usr/lib64/R/library/eRm/help/eRm.rdb
/usr/lib64/R/library/eRm/help/eRm.rdx
/usr/lib64/R/library/eRm/help/paths.rds
/usr/lib64/R/library/eRm/html/00Index.html
/usr/lib64/R/library/eRm/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/eRm/libs/eRm.so
/usr/lib64/R/library/eRm/libs/eRm.so.avx512
