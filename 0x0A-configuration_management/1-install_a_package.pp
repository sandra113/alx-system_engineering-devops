#installing flask from pip3
exec { 'install_upgrade_flask':
  command => 'pip3 install --upgrade Flask==2.1.0',
}
