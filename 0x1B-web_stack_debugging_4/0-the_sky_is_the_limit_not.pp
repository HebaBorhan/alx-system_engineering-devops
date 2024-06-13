# This script set a new value for ULIMIT

exec { 'update_ulimit_value':
  command => 'sed -i \'s/ULIMIT="-n 15"/ULIMIT="-n 4096"/\' /etc/default/nginx',
  path    => '/bin:/usr/bin',
}
