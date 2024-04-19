# First ensure pip3 is installed
exec { 'install Flask':
  command     => 'pip3 install Flask==2.1.0',
  unless      => 'pip3 freeze | grep Flask==2.1.0',
  path        => ['/usr/bin', '/bin'],
  provider    => 'shell',
}
