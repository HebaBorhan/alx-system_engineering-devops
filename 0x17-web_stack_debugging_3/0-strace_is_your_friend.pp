# Path to the wp-settings.php file
$file_path = '/var/www/html/wp-settings.php'

file { $file_path:
  ensure => file,
}

# Correcting typo in wp-settings.php file
exec { 'fix_php_typo':
  command => '/bin/sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" $file_path',
  require => File[$file_path],
}
