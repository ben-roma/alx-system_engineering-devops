# File:   7-puppet_install_nginx_web_server.pp
# Install and configure Nginx to serve a page with "Hello World!" and set up a 301 redirection

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  content => 'Hello World',
}

file_line { 'redirection-301':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => [Package['nginx'], File['/var/www/html/index.html']],
  subscribe => File['/var/www/html/index.html'],
}
