# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Maintainer: Menachem Mostowicz <moystovi@g.jct.ac.il>
pkgname=freedns-updater-git
pkgver=20120416
pkgrel=1
pkgdesc="Updates freedns.afraid.org dynamic dns domains"
arch=('any')
url="http://www.github.com/InvisibleEngineer/FreeDNS-Updater"
license=('custom:UNLICENSE')
depends=('python')
makedepends=('git')
install='INSTALL'
changelog='CHANGELOG'
source=('UNLICENSE')
md5sums=('464de46b424b82da11f364be1bb9411c')
_gitroot="git://github.com/InvisibleEngineer/FreeDNS-Updater.git"
_gitname=FreeDNS-Updater

build() {
  cd "$srcdir"
  msg "Connecting to GIT server...."

  if [[ -d "$_gitname" ]]; then
    cd "$_gitname" && git pull origin
    msg "The local files are updated."
  else
    git clone "$_gitroot" "$_gitname"
  fi

  msg "GIT checkout done or server timeout"
  msg "Starting install..."

  rm -rf "$srcdir/$_gitname-build"
  git clone "$srcdir/$_gitname" "$srcdir/$_gitname-build"
}

package() {
  cd "$srcdir/$_gitname-build"
  mkdir -p "$pkgdir/usr/bin/"
  install freedns.py "$pkgdir/usr/bin/"
  mkdir -p "$pkgdir/usr/share/licenses/$pkgname/"
  install UNLICENSE "$pkgdir/usr/share/licenses/$pkgname/"
}

# vim:set ts=2 sw=2 et:
