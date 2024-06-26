# Installe et configure Nginx avec Puppet

class { 'nginx': }

nginx::resource::server { 'default':
  ensure      => present,
  listen_port => 80,
  server_name => ['_'],
  proxy       => 'off',
  location_cfg_append => {
    'default_type' => 'text/html',
    'alias' => '/var/www/html',
  },
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => file,
  content => 'Ceci n\'est pas une page',
}

nginx::resource::location { '/redirect_me':
  ensure      => present,
  location    => '/redirect_me',
  proxy       => 'off',
  www_root    => '/var/www/html',
  rewrite     => '^ /https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent',
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => File['/var/www/html/index.html'],
}
