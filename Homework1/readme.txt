Stone Barrett
CSE 590 Python Data Analytics
Homework 1 Documentation

Problem 1: down(successprct, yardrange)
This method takes in a success percentage and yard range that are to be determined 
by an external testing script and returns an amount of yards gained in that down. 
All rules from the prompt are followed and my personal testing with this method
has shown it to be successful. I DID implement the extra credit option by providing a
chance for a sack or offensive penalty to take place. A sack results in -5 from the 
amount of yards returned and an offensive penalty results in -10. The two occuring on
the same down results in -15. It's been many years since I played football so I'm 
not sure if these values are accurate but they seem reasonable! 

Problem 2: drive(yards_to_TD, successprct, yardrange)
This method takes in the number of yards away from a touchdown, the chance of success,
and a yard range that are all to be determined by an external testing script. This 
method runs four downs and accounts for and implements all rules states by the prompt.
The method returns a tuple with the points scored and the position of the other team.
I DID implement extra credit options by accounting for first downs and handling cases
respectively.

Problem 3: drive_depicted(yards_to_TD, successprct, yardrange)
This method does exactly what the previous one does except it visually depicts what is
happening at the end of each down. The ball's position on the field is updated and the
down, yards remaining, and possible turnover or touchdown are printed. I did NOT implement
extra credit options as based on the prompt, I cannot score above 106 and the first two
problems may have me reach that already. This would have definitely been the most difficult
of the three options!

Problem 4: simulategame(num_drives, prctT1, yrangeT1, prctT2, yrangeT2)
This method takes in a number of drives to be played, success percentages for two teams,
and yard ranges for two teams, all of which to be determined by an external testing script.
It returns a tuple in the form of (team 1 score, team 2 score). All rules from the prompt
were followed.

Testing Script:
The script I used to test these functions is included in my submission. It runs many games
and keeps count of how many games are won by each team. 