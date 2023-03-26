# Client SSH configuration file

file { '/home/vagrant/.ssh/config':
  ensure  => file,
  mode    => '0600',
  content => "
Host 3.80.19.9
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
 ",
}
