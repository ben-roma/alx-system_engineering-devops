# Increase the ULIMIT in the /etc/default/nginx file

exec { 'increase-nginx-ulimit':
    command => 'sed -i "s/^ULIMIT=.*/ULIMIT=4096/" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/',
    onlyif  => 'grep -q "^ULIMIT=15" /etc/default/nginx',
    notify  => Exec['nginx-restart'],
}

# Restart Nginx

exec { 'nginx-restart':
    command     => '/etc/init.d/nginx restart',
    path        => '/sbin/:/usr/sbin/:/bin/:/usr/bin/',
    refreshonly => true,
}
