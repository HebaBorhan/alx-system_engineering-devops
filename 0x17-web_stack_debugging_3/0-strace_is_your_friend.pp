# Install Ruby
package { 'ruby':
  ensure => installed,
}

# Install puppet-lint gem
exec { 'install_puppet_lint':
  command => 'gem install puppet-lint -v 2.1.1',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'],
  require => Package['ruby'],
}

# Define the file path
$file_path = '/var/www/html/wp-settings.php'

# Ensure the file exists
file { $file_path:
  ensure => file,
}

# Correct the typo in the wp-settings.php file
exec { 'fix_php_typo':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' ${file_path}",
  require => File[$file_path],
}
