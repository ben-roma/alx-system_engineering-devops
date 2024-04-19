# First ensure pip3 is installed
exec { 'install-pip3':
  command => '/usr/bin/apt-get install -y python3-pip',
  unless  => 'dpkg -l | grep -qw python3-pip',
}

# Install Flask via pip3
exec { 'install-flask':
  command => '/usr/local/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/local/bin/pip3 freeze | grep -q "Flask==2.1.0"',
  require => Exec['install-pip3'], # Ensure pip3 is installed before running this
}
