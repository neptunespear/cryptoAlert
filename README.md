#cryptoTracker.py

1)run the python file 

2)enter your email and your password and the sender mail to send the details of the price of bitcoin 

3)enter the bitcoin name and alert amount for getting the mail(smptp).


#Approach Used

1)Define send mail function used to send the mail to the given email address using smtp which will further confirms that the mail is sent in our console

2)using the given api we have taken the data and loop through it and check whethet the id of the data matches to that of the name of bitcoin entered by us 

3)its check the current price of that bitoin and matches to the alert price entered by us and if it is less it again send the request to the given api every 120 secs for checking
  the price
  
4) while checking the price if it is less it also print the current price with the image of that crypto currency along with the name in our console

5)As soon  as the price is equal to the alert price entered by us it send the mail to the sender mail address provided by us from our mail address.

6) we will also get the message in our console with the crypto image and name and message.


