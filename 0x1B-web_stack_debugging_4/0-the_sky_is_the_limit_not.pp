# increse limits or tune nginx server to hhandle more requests

exec { '/etc/default/nginx':
  command => "/bin/echo ULIMIT='-n 5000' > /etc/default/nginx && /usr/bin/sudo\
  service nginx restart"
}
