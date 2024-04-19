# Filename: 0-create_a_file.pp
file { '/tmp/school':
  ensure  => 'file',                 # Ensures that it will be a file
  content => 'I love Puppet',        # Content of the file
  mode    => '0744',                 # File permission
  owner   => 'www-data',             # Owner of the file
  group   => 'www-data',             # Group of the file
}
