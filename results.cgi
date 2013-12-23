#!/usr/bin/perl
print "Content-Type: text/html\n\n";
open my $fh, "<", "results.txt";
print "<html><head>";
print "<title>Results from CSC 443 Perl Survey</title>";
print "</head><body>";

while(<$fh>)
	{
		$results = $results . $_;
	}
close $fh;
@b = split('/end', $results);
print <<ENDHTML;
<h2><center>RESULTS FROM SURVEY</center></h2>
<table align="center" style="margin-top:20%;border: groove 3px #0000ff">
<tbody>
<tr> 
<td style="text-align:center;border: groove 3px #0000ff"> # </td>
<td style="text-align: center;font-weight:bold;border:groove 2px #0000fe;background: #cdcdff"> 
Q1 
</td> 
<td style="text-align: center;font-weight:bold;border:groove 2px #0000fe;background: #cdcdff"> 
Q2 
</td> 
<td style="text-align: center;font-weight:bold;border:groove 2px #0000fe;background: #cdcdff"> 
Q3 
</td>
<td style="text-align: center;font-weight:bold;border:groove 2px #0000fe;background: #cdcdff">
Q4 
</td>
<td style="text-align: center;font-weight:bold;border:groove 2px #0000fe;background: #cdcdff"> 
Q5 
</td>
<td style="text-align: center;font-weight:bold;border:groove 2px #0000fe;background: #cdcdff"> 
Q6 
</td>
</tr>
<tr> 
<td style="text-align:center;border: groove 3px #ab00ff"> 
1. 
</td>
<td style="text-align:center;border: groove 3px #ab00ff"> 
@b[0] 
</td>
<td style="text-align:center;border: groove 3px #ab00ff"> 
@b[1] 
</td>
<td style="text-align:center;border: groove 3px #ab00ff"> 
@b[2] 
</td>
<td style="text-align:center;border: groove 3px #ab00ff"> 
@b[3] 
</td>
<td style="text-align:center;border: groove 3px #ab00ff"> 
@b[4] 
</td>
<td style="text-align:center;border: groove 3px #ab00ff"> 
@b[5] 
</td>
</tr>

</tbody>
</table>







ENDHTML

print "</body</html>";