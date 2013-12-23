#!/usr/bin/perl

print "Content-Type: text/html\n\n";
use CGI;
my $cgi = CGI->new;
&checkParam;
sub checkParam
{

	if($cgi->param("Q1"))
	{
		$q1 = $cgi->param("Name");

		&question2;
	}
elsif($cgi->param("Q2"))
	{
		$q1 = $cgi->param("Name");
		$q2 = $cgi->param("Q2_1");
		&question3;
	}
elsif($cgi->param("Q3"))
	{
		$q1 = $cgi->param("Name");
		$q2 = $cgi->param("Q2_1");
		$q3 = $cgi->param("Q3_1");
		&question4;
	}
elsif($cgi->param("Q4"))
	{
		$q1 = $cgi->param("Name");
		$q2 = $cgi->param("Q2_1");
		$q3 = $cgi->param("Q3_1");
		$q4 = $cgi->param("Q4_1");
		&question5;
	}
elsif($cgi->param("Q5"))
	{
		$q1 = $cgi->param("Name");
		$q2 = $cgi->param("Q2_1");
		$q3 = $cgi->param("Q3_1");
		$q4 = $cgi->param("Q4_1");
		$q5 = $cgi->param("Q5_1");
		&question6;
	}
elsif($cgi->param("Q6"))
	{
		$q1 = $cgi->param("Name");
		$q2 = $cgi->param("Q2_1");
		$q3 = $cgi->param("Q3_1");
		$q4 = $cgi->param("Q4_1");
		$q5 = $cgi->param("Q5_1");
		$q6 = $cgi->param("Q6_1");
		&lastPage;
	}
elsif($cgi->param("Q2_Back"))
	{
		$q1 = $cgi->param("Name");
		&question1;
	}
elsif($cgi->param("Q3_Back"))
	{
		$q1 = $cgi->param("Name");
		$q2 = $cgi->param("Q2_1");
		&question2;

	}
elsif($cgi->param("Q4_Back"))
	{
		$q1 = $cgi->param("Name");
		$q2 = $cgi->param("Q2_1");
		$q3 = $cgi->param("Q3_1");
		&question3;

	}
elsif($cgi->param("Q5_Back"))
	{
		$q1 = $cgi->param("Name");
		$q2 = $cgi->param("Q2_1");
		$q3 = $cgi->param("Q3_1");
		$q4 = $cgi->param("Q4_1");
		&question4;

	}
elsif($cgi->param("Q6_Back"))
	{
		$q1 = $cgi->param("Name");
		$q2 = $cgi->param("Q2_1");
		$q3 = $cgi->param("Q3_1");
		$q4 = $cgi->param("Q4_1");
		$q5 = $cgi->param("Q5_1");
		&question5;

	}
else
	{
		&question1;
	}

}

sub question1{
print "<html> <head>\n";
print "<title>CSC 443 Perl Survey!</title>";
print "</head>\n";
print "<body bgcolor='ABB0B3'><br><br><br>\n";
print "<div id='first_question' style='display:block'>";
print "<center><font size='20'>1.	Please enter your name</font><br>";
print "<form method='post' action='survey.cgi'>";
if($q1)
	{
	print "<textarea name='Name'> $q1 </textarea><br>";
	}
else
	{
print "<textarea name='Name'></textarea><br>";
	}
print "<input type='submit' value='Next' name='Q1'>";
print "</form>";
print "</center>";
print "</div>";
}

sub question2
{
print "<html> <head>\n";
print "<title>CSC 443 Perl Survey Question 2</title>";
print "</head>\n";
print "<body bgcolor='ABB0B3'><br><br><br>\n";
print "<div id='buttons' style='float:right'>";
print "<form method='post' action='survey.cgi'>";
print "<input type='submit' value='Prev' name=Q2_Back>";
print "<input type='submit' value='Next' name='Q2'>";
print "</div><br><br><br>";
print "<center><font size='20'>2.	Did you find the information within this website useful?</font><br>";
print "<input type=hidden name=Name value=$q1>";
print "<table border='1' cellspacing='0' cellpadding='10px' style='border-collapse:collapse'>";
if($q2)
	{
		if($q2 == 1){
			print "<tr>";
			print "<td align=center>";
			print "<input type=radio value='1' name=Q2_1 checked> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='2' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='3' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='4' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='5' name=Q2_1> \t";
			print "</td>";
			print "</tr>";
		}
	elsif($q2 == 2)
		{
			print "<tr>";
			print "<td align=center>";
			print "<input type=radio value='1' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='2' name=Q2_1 checked> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='3' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='4' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='5' name=Q2_1> \t";
			print "</td>";
			print "</tr>";
		}
	elsif($q2 == 3){
			print "<tr>";
			print "<td align=center>";
			print "<input type=radio value='1' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='2' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='3' name=Q2_1 checked> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='4' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='5' name=Q2_1> \t";
			print "</td>";
			print "</tr>";
		}
	elsif($q2 == 4){
			print "<tr>";
			print "<td align=center>";
			print "<input type=radio value='1' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='2' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='3' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='4' name=Q2_1 checked> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='5' name=Q2_1> \t";
			print "</td>";
			print "</tr>";
		}
	elsif($q2 == 5){
			print "<tr>";
			print "<td align=center>";
			print "<input type=radio value='1' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='2' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='3' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='4' name=Q2_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='5' name=Q2_1 checked> \t";
			print "</td>";
			print "</tr>";
		}
	}


else{
print "<tr>";
print "<td align=center>";
print "<input type=radio value='1' name=Q2_1> \t";
print "</td>";
print "<td align=center>";
print "<input type=radio value='2' name=Q2_1> \t";
print "</td>";
print "<td align=center>";
print "<input type=radio value='3' name=Q2_1> \t";
print "</td>";
print "<td align=center>";
print "<input type=radio value='4' name=Q2_1> \t";
print "</td>";
print "<td align=center>";
print "<input type=radio value='5' name=Q2_1> \t";
print "</td>";
print "</tr>";
}
print "<tr>";
print "<td align=center>";
print "1\t";
print "</td>";
print "<td align=center>";
print "2\t";
print "</td>";
print "<td align=center>";
print "3\t";
print "</td>";
print "<td align=center>";
print "4\t";
print "</td>";
print "<td align=center>";
print "5\t";
print "</td>";
print "</tr>";
print "<tr>";
print "<td align=center>";
print "Not at all\t";
print "</td>";
print "<td align=center>";
print "\t";
print "</td>";
print "<td align=center>";
print "Somewhat\t";
print "</td>";
print "<td align=center>";
print "\t";
print "</td>";
print "<td align=center>";
print "Extremely\t";
print "</td>";
print "</tr>";
print "<table>";
print "</form>";
print "</center>";
print "</body>";
print "</html>";

}
sub question3
{
print "<html> <head>\n";
print "<title>CSC 443 Perl Survey Question 3</title>";
print "</head>\n";
print "<body bgcolor='ABB0B3'><br><br><br>\n";
print "<div id='buttons' style='float:right'>";
print "<form method='post' action='survey.cgi'>";
print "<input type='submit' value='Prev' name=Q3_Back>";
print "<input type='submit' value='Next' name='Q3'>";
print "</div><br><br><br>";
print "<center><font size='20'>3.	Is this website easy to navigate?</font><br>";
print "<input type=hidden name=Name value=$q1>";
print "<input type=hidden name=Q2_1 value=$q2>";
print "<table border='1' cellspacing='0' cellpadding='10px' style='border-collapse:collapse'>";
if($q3)
	{
		if($q3 == 1){
			print "<tr>";
			print "<td align=center>";
			print "<input type=radio value='1' name=Q3_1 checked> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='2' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='3' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='4' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='5' name=Q3_1> \t";
			print "</td>";
			print "</tr>";
		}
	elsif($q3 == 2)
		{
			print "<tr>";
			print "<td align=center>";
			print "<input type=radio value='1' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='2' name=Q3_1 checked> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='3' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='4' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='5' name=Q3_1> \t";
			print "</td>";
			print "</tr>";
		}
	elsif($q3 == 3){
			print "<tr>";
			print "<td align=center>";
			print "<input type=radio value='1' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='2' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='3' name=Q3_1 checked> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='4' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='5' name=Q3_1> \t";
			print "</td>";
			print "</tr>";
		}
	elsif($q3 == 4){
			print "<tr>";
			print "<td align=center>";
			print "<input type=radio value='1' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='2' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='3' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='4' name=Q3_1 checked> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='5' name=Q3_1> \t";
			print "</td>";
			print "</tr>";
		}
	elsif($q3 == 5){
			print "<tr>";
			print "<td align=center>";
			print "<input type=radio value='1' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='2' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='3' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='4' name=Q3_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='5' name=Q3_1 checked> \t";
			print "</td>";
			print "</tr>";
		}
	}


else{
print "<tr>";
print "<td align=center>";
print "<input type=radio value='1' name=Q3_1> \t";
print "</td>";
print "<td align=center>";
print "<input type=radio value='2' name=Q3_1> \t";
print "</td>";
print "<td align=center>";
print "<input type=radio value='3' name=Q3_1> \t";
print "</td>";
print "<td align=center>";
print "<input type=radio value='4' name=Q3_1> \t";
print "</td>";
print "<td align=center>";
print "<input type=radio value='5' name=Q3_1> \t";
print "</td>";
print "</tr>";
}
print "<tr>";
print "<td align=center>";
print "1\t";
print "</td>";
print "<td align=center>";
print "2\t";
print "</td>";
print "<td align=center>";
print "3\t";
print "</td>";
print "<td align=center>";
print "4\t";
print "</td>";
print "<td align=center>";
print "5\t";
print "</td>";
print "</tr>";
print "<tr>";
print "<td align=center>";
print "Not at all\t";
print "</td>";
print "<td align=center>";
print "\t";
print "</td>";
print "<td align=center>";
print "Somewhat\t";
print "</td>";
print "<td align=center>";
print "\t";
print "</td>";
print "<td align=center>";
print "Extremely\t";
print "</td>";
print "</tr>";
print "<table>";
print "</form>";
print "</center>";
print "</body>";
print "</html>";

}

sub question4
{

print "<html> <head>\n";
print "<title>CSC 443 Perl Survey Question 4</title>";
print "</head>\n";
print "<body bgcolor='ABB0B3'><br><br><br>\n";
print "<div id='buttons' style='float:right'>";
print "<form method='post' action='survey.cgi'>";
print "<input type='submit' value='Prev' name=Q4_Back>";
print "<input type='submit' value='Next' name='Q4'>";
print "</div><br><br><br>";
print "<center><font size='20'>4.	Were you able to find the information you were looking for?</font><br>";
print "<input type=hidden name=Name value=$q1>";
print "<input type=hidden name=Q2_1 value=$q2>";
print "<input type=hidden name=Q3_1 value=$q3>";
print "<table border='1' cellspacing='0' cellpadding='10px' style='border-collapse:collapse'>";
if($q4)
	{
		if($q4 == 1)
		{
		print "<tr>";
		print "<td align=center>";
		print "<input type=radio value='1' name=Q4_1 checked> \t";
		print "</td>";
		print "<td align=center>";
		print "<input type=radio value='2' name=Q4_1> \t";
		print "</td>";
		print "<td align=center>";
		print "<input type=radio value='0' name=Q4_1> \t";
		print "</td>";
		print "</tr>";
		}
	elsif($q4 == 2)
		{
			print "<tr>";
			print "<td align=center>";
			print "<input type=radio value='1' name=Q4_1> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='2' name=Q4_1 checked> \t";
			print "</td>";
			print "<td align=center>";
			print "<input type=radio value='0' name=Q4_1> \t";
			print "</td>";
			print "</tr>";
		}
}
else
	{
print "<tr>";
print "<td align=center>";
print "<input type=radio value='1' name=Q4_1> \t";
print "</td>";
print "<td align=center>";
print "<input type=radio value='2' name=Q4_1> \t";
print "</td>";
print "<td align=center>";
print "<input type=radio value='0' name=Q4_1 checked> \t";
print "</td>";
print "</tr>";
}
print "<tr>";
print "<td align=center>";
print "1\t";
print "</td>";
print "<td align=center>";
print "2\t";
print "</td>";
print "<td align=center>";
print "0\t";
print "</td>";
print "</tr>";
print "<tr>";
print "<td align=center>";
print "Yes\t";
print "</td>";
print "<td align=center>";
print "No\t";
print "</td>";
print "<td align=center>";
print "N/A\t";
print "</td>";
print "</tr>";
print "<table>";
print "</form>";
print "</center>";
print "</body>";
print "</html>";

}

sub question5
{

print "<html> <head>\n";
print "<title>CSC 443 Perl Survey Question 5</title>";
print "</head>\n";
print "<body bgcolor='ABB0B3'><br><br><br>\n";
print "<div id='buttons' style='float:right'>";
print "<form method='post' action='survey.cgi'>";
print "<input type='submit' value='Prev' name=Q5_Back>";
print "<input type='submit' value='Next' name='Q5'>";
print "</div><br><br><br>";
print "<center><font size='20'>5.	What other information would you like to be included in the web site?</font><br>";
print "<input type=hidden name=Name value=$q1>";
print "<input type=hidden name=Q2_1 value=$q2>";
print "<input type=hidden name=Q3_1 value=$q3>";
print "<input type=hidden name=Q4_1 value=$q4>";
if($q5)
	{
	print "<textarea rows=8 cols=30 name=Q5_1>$q5</textarea>";

	}
else
	{
	print "<textarea rows=8 cols=30 name=Q5_1></textarea>";
	}
print "</form>";
print "</center>";
print "</body>";
print "</html>";

}

sub question6
{

print "<html> <head>\n";
print "<title>CSC 443 Perl Survey Question 6</title>";
print "</head>\n";
print "<body bgcolor='ABB0B3'><br><br><br>\n";
print "<div id='buttons' style='float:right'>";
print "<form method='post' action='survey.cgi'>";
print "<input type='submit' value='Prev' name=Q6_Back>";
print "<input type='submit' value='Next' name='Q6'>";
print "</div><br><br><br>";
print "<center><font size='20'>6.	What suggestions might you have for our web site improvement?</font><br>";
print "<input type=hidden name=Name value=$q1>";
print "<input type=hidden name=Q2_1 value=$q2>";
print "<input type=hidden name=Q3_1 value=$q3>";
print "<input type=hidden name=Q4_1 value=$q4>";
print "<input type=hidden name=Q5_1 value=$q5>";
print "<textarea rows=8 cols=30 name=Q6_1></textarea>";
print "</form>";
print "</center>";
print "</body>";
print "</html>";

}

sub lastPage
{
my $filename = "results.txt";
open my $fh, ">", $filename;
print $fh "$q1"."/end"."$q2"."/end"."$q3"."/end"."$q4"."/end"."$q5"."/end"."$q6";
close $fh;
print "<html> <head>\n";
print "<title>CSC 443 Perl Survey Final Page</title>";
print "</head>\n";
print "<body bgcolor='ABB0B3'><br><br><br>\n";
print "<div id='lastPage' style='display:block'>";
print "<center><font size='20'>Thank you for your input.</font><br>";
print "</center>";
print "</div>";
print "</body>";
print "</html>";

}