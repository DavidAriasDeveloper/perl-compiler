#!/usr/bin/perl
use DBI;

my $database='dbi:DB2:sample';
my $user='';
my $password='';

my $dbh = DBI->connect($database, $user, $password)
  or die "Can't connect to $database: $DBI::errstr";

my $sth = $dbh->prepare(
  q{ SELECT firstnme, lastname
     FROM employee }
  )
  or die "Can't prepare statement: $DBI::errstr";

my $rc = $sth->execute
  or die "Can't execute statement: $DBI::errstr";

print "Query will return $sth->{NUM_OF_FIELDS} fields.\n\n";
print "$sth->{NAME}->[0]: $sth->{NAME}->[1]\n";

while (($firstnme, $lastname) = $sth->fetchrow()) {
  print "$firstnme: $lastname\n";
}

# comprobar si hay problemas que puedan haber cancelado antes la captación
warn $DBI::errstr if $DBI::err;

$sth->finish;
$dbh->disconnect;
