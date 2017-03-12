# DjangoLoginAuthAPI
Django API for login authentication , interaction with SQLite DB and Django Forms


This is the Django API . In this api we are extracting some of the fields from the database and verifying the values of the attributes from the url. If the values match then a successful JSON result is passed from this API and if they do not then an error message is passed in JSON format.

In this the sample database has the following attributes: Username -Primary key, password, name, Authentication key- that is the access token

There are 4 main events happening here : 1)sign up 2)login 3) Verify user 4)Form

In the sign up, username, password and name is entered by the user and an error would be displayed if the username already exists.

In login, a random access token(Authentication key) would be generated and used throught the session and deleted on logout. Advantage of access token is that we need not send password of the user everytime and hence security is not compomised.

Presently, GET method is used. But another HTMl file(a.HTML) is also created (not needed as of now) , in case we need to use POST method in future if required.

LoginAuth was the main file and will redirect the URL to Login...

Then another Important part is "Form" part. I have created forms using Django . The main focus is on the processing and backend. 
In this I have created a form to be filled where after filling required fields it is entered in the dataabse 
and then through POST method it is returned.
