# Filename: 1-install_a_package.pp
package { 'lask':
  ensure   => '2.1.0',                # Specifies the version of Flask to install
  provider => 'pip3',                 # Specifies that pip3 should be used to install the package
}
