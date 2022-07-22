# davisPutmamSolver
The input to the Davis-Putnam procedure has the following form: An atom is
denoted by a natural number: 1, 2, 3, .... For example, you can think 1 as
referring to the literal P and -1 as referring to the literal 6=P. A clause is a line
of text containing the integers of the corresponding literals. After all the clauses
have been given, the next line is the single value 0; anything further in the file
is ignored in the execution of the procedure and reproduced at the end of the
output file. (This allows for passing extra information in case the Davis-Putnam
procedure is a part of a larger pipeline of procedures to accomplish a task).
The output from the Davis-Putnam procedure has the following form: First, a
list of pairs of atoms (a natural number) and a truth value (either T or F). Second
a line containing the single value 0. Third, the remaining lines after the 0 line in
the input file reproduced exactly.
Example Input: Given the input:
1 2 3
-2 3
-3
0
This is a simple example with 3 clauses and 3 atoms.
Reproduce this line.
