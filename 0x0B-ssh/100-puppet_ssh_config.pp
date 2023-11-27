# Client SSH configuration file

file { '/home/user/.ssh/config':
  ensure  => file,
  owner   => 'user',
  group   => 'user',
  mode    => '0600',
  content => "
Host 100.26.225.70 
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
 ",
}
