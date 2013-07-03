Name:           weirdrouter
Version:        3.0.0
Release:        145%{?dist}
Summary:        The "Hello World" program from GNU
License:        GPLv3+
URL:            https://github.com/hordecore/weirdrouter
Source0:        weirdrouter_rpm_src.tar.gz

%prep
%setup -q
%build

mkdir -p /root/rpmbuild/BUILDROOT/%{name}-%{version}-%{release}.x86_64/
cp -varup /root/rpmbuild/BUILD/%{name}-%{version}/* /root/rpmbuild/BUILDROOT/%{name}-%{version}-%{release}.x86_64/

%files 
%defattr(-, root, root)
/root/testfile

%description
Простой в установке и интеграции роутер на базе стандартного CentOS 6

Основные идеи
- Никаких патчей и так далее, доверяемся тому, что в репозиториях
- Всё что нужно - указываем в зависимостях
- Предоставляется как есть, никакой поддержки, разве что за пиво
- Простое и документированное API, максимум возможностей по управлению
- Только стандартные программы, никаких своих доработок, даже если они что-то ускоряют

%changelog
* Wed 3 Jul Oleg Strizhechenko
- First RPM-build
