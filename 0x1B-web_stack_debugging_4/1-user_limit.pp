# This script updates soft and hard limits

exec { 'update_soft_limit':
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4096/" /etc/security/limits.conf',
  path    => '/bin:/usr/bin',
}

exec { 'update_hard_limit':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 8192/" /etc/security/limits.conf',
  path    => '/bin:/usr/bin',
}
