# 100-puppet_ssh_config.pp
# Configures the SSH client to use a specific private key and disable password authentication

# Ensure the puppetlabs-stdlib module is installed:
# puppet module install puppetlabs-stdlib

file { '/etc/ssh/ssh_config':
    ensure => file,
    owner  => 'root',
    group  => 'root',
    mode   => '0644',
}

# Declare the identity file used for SSH authentication
file_line { 'Declare identity file':
    path    => '/etc/ssh/ssh_config',
    line    => 'IdentityFile ~/.ssh/school',
    match   => '^IdentityFile',
    replace => true,
}

# Turn off password authentication
file_line { 'Turn off passwd auth':
    path    => '/etc/ssh/ssh_config',
    line    => 'PasswordAuthentication no',
    match   => '^PasswordAuthentication',
    replace => true,
}
