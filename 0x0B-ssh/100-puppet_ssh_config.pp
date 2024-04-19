# 100-puppet_ssh_config.pp

# Ensure the .ssh directory exists
file { '/home/ubuntu/.ssh':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0700',
}

# Manage the SSH configuration file
file { '/home/ubuntu/.ssh/config':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => epp('ssh_config.epp'),
}

# Manage the content of the SSH configuration with EPP template
file { '/etc/puppetlabs/code/environments/production/modules/ssh_config.epp':
  ensure  => 'file',
  content => @("EOF"/L)
    Host *
      IdentityFile /home/ubuntu/.ssh/school
      PasswordAuthentication no
    | EOF
}
