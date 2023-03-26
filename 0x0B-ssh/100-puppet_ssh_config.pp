#use Puppet to edit config file
include stdlib

File_line { 'Turn off passwd auth':
  path  => '/etc/ssh/sshd_config',
  line  => 'PasswordAuthentication no',
  match => '^#PasswordAuthentication yes',
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/sshd_config',
  line  => 'IdentityFile ~/.ssh/school',
  match => '^#IdentityFile ~/.ssh/id_rsa',
}
