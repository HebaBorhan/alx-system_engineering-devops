# This script configures a new Ubuntu machine to Install nginx on server
# then configure it so that its HTTP response contains a custom header

package { 'nginx':
  ensure => installed,
}

# custom headr of HTTP
$server_hostname = $::hostname

# Configure Nginx site
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location / {
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        add_header X-Served-By $server_hostname;
    }
}",
  notify  => Service['nginx'],
}

# Create symlink
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
