package Szywiecki;

$Robert = "el jefe";

sub terminate {
  my $name = shift;
  print "$Robert ha despedido a ${name}\n";
}

terminate("arturo"); # muestra "el jefe ha despedido a arturo"
