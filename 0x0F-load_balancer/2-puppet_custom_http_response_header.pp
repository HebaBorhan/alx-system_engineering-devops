# This script configures a new Ubuntu machine to Install nginx on server
# then configure it so that its HTTP response contains a custom header

package { 'nginx':
  ensure => installed,
}

# Define a custom fact to retrieve the hostname
Facter.add('server_hostname') do
  setcode 'hostname -s'
end

# Configure Nginx site
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;

      server_name _;

      add_header X-Served-By ${server_hostname};

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
