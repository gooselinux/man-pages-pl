%define releasedate 24-10-2005
Summary: Polish man pages from the Linux Documentation Project
Name: man-pages-pl
Version: 0.24
Release: 8.1%{?dist}
# No clear versioning.
License: GPL+
Group: Documentation
# the source is not available on any public mirror now
Source: man-PL%{releasedate}.tar.gz
Patch1: man-pages-pl-0.24-pidof.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArchitectures: noarch

%description
Manual pages from the Linux Documentation Project, translated into
Polish.

%prep
%setup -q -n pl_PL
%patch1 -p1

%build

%install
rm -fr $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/pl/man{1,2,3,4,5,6,7,8,9,n}
for i in FAQ man[1-8]/*.?; do
        iconv -f LATIN2 -t UTF-8 < $i > $i.new
        mv -f $i.new $i
done
for i in man[1-8] ; do 
    install -m 644 $i/*.? $RPM_BUILD_ROOT%{_mandir}/pl/$i; 
done
rm -f $RPM_BUILD_ROOT/%{_mandir}/pl/man8/rpm*

# too buggy to ship... not only errors, but also things which
# obviously don't work as the author intended
rm -f $RPM_BUILD_ROOT%{_mandir}/pl/man5/lisp-tut*

rm -f $RPM_BUILD_ROOT%{_mandir}/pl/man1/newgrp.1*
rm -f $RPM_BUILD_ROOT%{_mandir}/pl/man1/{apropos.1,chage.1,gendiff.1,gpasswd.1,man.1,mplayer.1,sg.1,whatis.1}*
rm -f $RPM_BUILD_ROOT%{_mandir}/pl/man1/{evim,ex,rview,rvim,view,vim,vimdiff,vimtutor}.1*
rm -f $RPM_BUILD_ROOT%{_mandir}/pl/man5/{faillog.5,shadow.5,man.config.5,qmail-*.5,dot-qmail.5}*
rm -f $RPM_BUILD_ROOT%{_mandir}/pl/man7/qmail.7*
rm -f $RPM_BUILD_ROOT%{_mandir}/pl/man8/{grpunconv.8,faillog.8,newusers.8,rpmcache.8,rpm2cpio.8,rpmdeps.8,rpm.8,rpmbuild.8,rpmgraph.8,pwconv.8,lastlog.8,stunnel.8,pwck.8,grpck.8,chpasswd.8,grpconv.8,adduser.8,pwunconv.8,groupadd.8,groupdel.8,groupmod.8,useradd.8,userdel.8,usermod.8,qmail}*

rm -f $RPM_BUILD_ROOT%{_mandir}/pl/man1/mc.1*

# Part of shadow-utils
rm -f $RPM_BUILD_ROOT%{_mandir}/pl/man5/login.defs.5*
rm -f $RPM_BUILD_ROOT%{_mandir}/pl/man8/groupmems.8*

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc FAQ
%dir %{_mandir}/pl
%{_mandir}/pl/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.24-8.1
- Rebuilt for RHEL 6

* Fri Oct  9 2009 Ivana Varekova <varekova@redhat.com> - 0.24-8
- fix source tag

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug  7 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.24-5
- fix license tag

* Mon Dec 17 2007 Ivana Varekova <varekova@redhat.com> - 0.24-4
- remove groupmems.8 (#425778)

* Fri Mar  2 2007 Ivana Varekova <varekova@redhat.com> - 0.24-3
- Resolves: 226128
  incorporate package review feedback

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 0.24-2.1
- rebuild

* Thu Apr 06 2006 Karsten Hopp <karsten@redhat.de> 0.24-2
- remove some vim man pages provided by current vim

* Mon Jan  9 2006 Ivana Varekova <varekova@redat.com> 0.24-1
- update source
- add pidof patch (created by Marcin Garski)

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Sep 26 2005 Ivana Varekova <varekova@redhat.com> 0.23-7
- login.defs man page removed (bug 169181), will be provided 
  by shadow-utils

* Thu Apr 07 2005 Peter Vrabec <pvrabec@redhat.com> 0.23-6
- newgrp man page removed, will be provided by shadow-utils

* Thu Nov 18 2004 Adrian Havill <havill@redhat.com> 0.23-4
- remove mc.1 (#138865)

* Wed Sep 29 2004 Adrian Havill <havill@redhat.com> 0.23-2
- bump n-v-r, rebuild

* Wed Apr 07 2004 Karsten Hopp <karsten@redhat.com>
- use new tarball from ptm.linux.pl (#112253)
- disable rofffix patch

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Feb 10 2004 Akira TAGOH <tagoh@redhat.com> 0.22-14
- removed apropos.1, man.1, whatis.1, and man.config.5, because the latest man contains those manpages.

* Tue Feb 11 2003 Phil Knirsch <pknirsch@redhat.com> 0.22-13
- Convert all manpages to utf-8.

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Nov 25 2002 Tim Powers <timp@redhat.com>
- remove man pages which conflict with shadow-utils

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Aug  2 2001 Trond Eivind Glomsrød <teg@redhat.com>
- s/Copyright/License/
- Own %%{_mandir}/pl

* Wed Apr  4 2001 Trond Eivind Glomsrød <teg@redhat.com>
- fix roff errors in various man pages (#34189)
- remove lisp-tut.5 - it's beyond repair and needs rewriting

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 20 2000 Jeff Johnson <jbj@redhat.com>
- rebuild to compress man pages.

* Mon Jun 19 2000 Trond Eivind Glomsrød <teg@redhat.com>
- don't include rpm manpage, it's included with rpm

* Sun Jun 11 2000 Trond Eivind Glomsrød <teg@redhat.com>
- fixed typo in description
* Sun Jun 11 2000 Trond Eivind Glomsrød <teg@redhat.com>
- first build
