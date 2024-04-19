# install Flask -v 2.1.0

exec { 'install specific version of flask using pip3':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 freeze | grep Flask==2.1.0',
  path    => ['/usr/bin', '/bin'],
}
