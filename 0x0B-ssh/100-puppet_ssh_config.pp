# This script shows the SSH client configuration

file { '/home/heba/.ssh/config':
  ensure => present,
  content => "\
Host 23.23.73.165
    IdentityFile ~/.ssh/school
    PreferredAuthentications publickey
    PasswordAuthentication no
",
  owner => 'heba',
  group => 'heba',
  mode => '0600',
}
