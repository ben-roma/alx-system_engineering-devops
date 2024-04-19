# Puppet manifest to install Flask version 2.1.0 using pip3
class flask_install {
  package { 'Flask':
    ensure   => '2.1.0',
    provider => 'pip3',
  }
}

include flask_install
