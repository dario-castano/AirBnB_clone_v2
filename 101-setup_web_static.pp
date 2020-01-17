# Configure a nginx server with header
exec {'apt_update':
  command => 'apt-get update -y',
  path    => '/usr/bin/'
}

group { 'ubuntu':
  ensure => 'present'
}

user { 'ubuntu':
  ensure  => 'present',
  groups  => 'ubuntu',
  require => Group['ubuntu']
}

file{'/data':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => User['ubuntu']
}

file{'/data/web_static':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => User['ubuntu']
}

file{'/data/web_static/releases':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => User['ubuntu']
}

file{'/data/web_static/shared':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => User['ubuntu']
}

file{'/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => User['ubuntu']
}

file{'/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  require => File['/data/web_static/releases/test']
}

exec{'download_fakehtml':
  command => '/usr/bin/wget -q https://raw.githubusercontent.com/dario-castano/AirBnB_clone_v2/master/fake.html -O /data/web_static/releases/test/index.html',
  require => File['/data/web_static/releases/test']
}

package{'nginx':
  ensure   => 'installed',
  name     => 'nginx',
  provider => 'apt',
  require => Exec['apt_update']
}

exec{'download_conf':
  command => '/usr/bin/wget -q https://raw.githubusercontent.com/dario-castano/AirBnB_clone_v2/master/default.txt -O /etc/nginx/sites-available/default',
  require => Package['nginx']
}

service{'nginx_service':
  ensure  => 'running',
  name    => 'nginx',
  enable  => 'true',
  require => [Package['nginx'], Exec['download_conf']]
}

file{'/etc/nginx/sites-available/default':
  notify  => Service['nginx_service'],
  require => Package['nginx']
}
