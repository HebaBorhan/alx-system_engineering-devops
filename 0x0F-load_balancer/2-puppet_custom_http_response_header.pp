# This script configures new Ubuntu machine to Install nginx on server
# then configure it so that its HTTP response contains a custom header

package { 'nginx':
  ensure => installed,
}

# Configure Nginx site
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;

      server_name _;

      add_header X-Served-By ${facts['hostname']};

      location / {
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
      }
    }
  ",
  require => Package['nginx'],
}

# Restart Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}

# Check if custom header is present in Nginx response
exec { 'check_nginx_custom_header':
  command     => '/usr/bin/curl -Is http://localhost | grep -q "X-Served-By"',
  path        => ['/bin', '/usr/bin'],
  logoutput   => true,
  refreshonly => true,
  subscribe   => Service['nginx'],
}
