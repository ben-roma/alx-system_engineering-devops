# Filename: 1-install_a_package.pp

exec { 'install_flask':
    command => '/usr/bin/pip3 install flask==2.1.0',
    path    => ['/usr/bin', '/bin'],
    unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}

exec { 'install_werkzeug':
    command => '/usr/bin/pip3 install werkzeug==2.1.1',
    path    => ['/usr/bin', '/bin'],
    unless  => '/usr/bin/pip3 show werkzeug | grep -q "Version: 2.1.1"',
}
