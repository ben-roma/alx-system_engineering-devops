# Filename: 1-install_a_package.pp
package { 'python3-pip':
  ensure   => installed,
}

# Ensure Flask is installed at a specific version via pip
exec { 'install-flask':
  command     => 'pip3 install Flask==2.1.0',
  unless      => 'pip3 freeze | grep Flask==2.1.0',
  require     => Package['python3-pip'], # Ensures pip is installed first
}
