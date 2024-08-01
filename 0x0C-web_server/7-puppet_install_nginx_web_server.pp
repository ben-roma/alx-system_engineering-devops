# Manifeste Puppet pour installer et configurer Nginx

class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => "<html>
<head>
    <title>Welcome to Nginx!</title>
</head>
<body>
    <h1>Hello World!</h1>
</body>
</html>",
  }

  file { '/var/www/html/404.html':
    ensure  => file,
    content => "<html>
<head>
    <title>404 Not Found</title>
</head>
<body>
    <h1>Ceci n'est pas une page</h1>
</body>
</html>",
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-available/default'],
  }
}

node default {
  include nginx
}
