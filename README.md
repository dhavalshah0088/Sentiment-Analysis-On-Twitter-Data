# Sentiment-Analysis-On-Twitter-Data

1.	Create a twitter account if you do not already have one.
2.	Go to https://dev.twitter.com/apps and log in with your twitter credentials.
3.	Click "Create New App"
4.	Fill out the form and agree to the terms. Put in a dummy website if you don't have one you want to use.
5.	On the next page, click the "API Keys" tab along the top, then scroll all the way down until you see the section "Your Access Token"
6.	Click the button "Create My Access Token". 
7.	You will now copy four values into twitterstream.py. These values are your "API Key", your "API secret", your "Access token" and your "Access token secret". All four should now be visible on the API Keys page. (You may see "API Key" referred to as "Consumer key" in some places in the code or on the web; they are synonyms.) Open twitterstream.py and set the variables corresponding to the api key, api secret, access token, and access secret. You will see code like the below:
8.	api_key = "<Enter api key>"
api_secret = "<Enter api secret>"
access_token_key = "<Enter your access token key here>"
access_token_secret = "<Enter your access token secret here>"
9.	Run the following and make sure you see data flowing and that no errors occur.
        $ python twitterstream.py > output.txt
        The twitter data file collected is 164.3 mb.
