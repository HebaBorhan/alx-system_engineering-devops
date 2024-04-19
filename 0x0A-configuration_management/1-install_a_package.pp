#Install flask

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.1.1',
  path    => ['/usr/bin', '/usr/local/bin'],
  unless  => '/usr/bin/pip3 show Werkzeug | grep -q "Version: 2.1.1"',
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin', '/usr/local/bin'],
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  require => Exec['install_werkzeug'],
}
