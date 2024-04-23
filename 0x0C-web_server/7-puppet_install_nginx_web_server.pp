# This script is used to  to install and configure an Nginx

package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
    server {
      listen 80;
      server_name _;

      location / {
        return 200 'Hello World!';
      }

      location /redirect_me {
        return 301 https://www.example.com/;
      }
    }
  ",
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
