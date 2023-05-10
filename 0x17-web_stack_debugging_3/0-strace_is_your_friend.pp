# Fix 500 error on request to Apache web server

exec {'substitue':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
