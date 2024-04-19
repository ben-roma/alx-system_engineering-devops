# Puppet manifest to install Flask version 2.1.0 using pip3
class flask_install {
  package { 'python3-pip':
    ensure => installed,
  }

  exec { 'install Flask':
    command     => 'pip3 install Flask==2.1.0',
    unless      => 'pip3 freeze | grep Flask==2.1.0',
    path        => ['/usr/bin', '/bin'],
    require     => Package['python3-pip'],  # Ensure pip is installed first
  }
}

include flask_install
