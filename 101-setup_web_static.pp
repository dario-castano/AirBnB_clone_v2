# Configure a nginx server with header

file{'/data':
  ensure => 'directory',
  owner  => 'ubuntu'
  group  => 'ubuntu'
}

file{'/data/web_static':
  ensure => 'directory',
  owner  => 'ubuntu'
  group  => 'ubuntu'
}

file{'/data/web_static/releases':
  ensure => 'directory',
  owner  => 'ubuntu'
  group  => 'ubuntu'
}

file{'/data/web_static/shared':
  ensure => 'directory',
  owner  => 'ubuntu'
  group  => 'ubuntu'
}

file{'/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'ubuntu'
  group  => 'ubuntu'
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
  ensure   => 'installed'
  name     => 'nginx',
  provider => 'apt',
}

exec{'download_conf':
  command => '/usr/bin/wget -q https://raw.githubusercontent.com/dario-castano/AirBnB_clone_v2/master/default.txt -O /etc/nginx/nginx.conf',
  require => Package['nginx']
}

service{'nginx_service':
  ensure  => 'running',
  name    => 'nginx',
  enable  => 'true',
  require => [Package['nginx'], Exec['download_conf']]
}

file{'/etc/nginx/nginx.conf':
  notify  => Service['nginx_service'],
  require => Package['nginx']
}
