# chaseAshbySeniorDesign

## Team Members
* Chase Ashby

## Contact Information
* Ashbych@mail.uc.edu

## Project Advisor
* Fred Annexstein 

## Work Completed
* Completed upwards of 15 hours doing research on covid channels.
* Spent 5-6 hours designing the network covert channel.
* Spent 10 hours creating the receiving side and setting up an environment.
* Spent 5 hours on the implementation of the sending side.
* Spent 5 hours creating presentations and other tasks.

# How does it work?
My covert channel works by setting a destination server and port. Then reading in text data,
it then converts that information to binary and attaches it to a TCP header and send it 
to another server where the attached information is retrieved then output in binary form. After
that is converted back to it's original messsage and output again. All this is done unknown
to the user.

