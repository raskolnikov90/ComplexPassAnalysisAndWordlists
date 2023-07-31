# Analysis and Creation of Wordlists with Complex Passwords for Password Cracking
There is a lot of research and statistics on the most common passwords which tend to be the least safe, like “12345”, the word “password” itself and others. Many famous wordlists coming from data breaches or cybersecurity research contain such passwords, however the focus of my research is to look more into complex passwords while ignoring the simpler common insecure passwords, find what common features more complex passwords have and create new wordlists to crack complex passwords.
I define complex password as having at least three of the following:
-Contains 8 letters or more
-Contains numbers
-Contains uppercase letters
-Contains special characters

1-The Collected Complex Passwords Wordlist
My first objective was to make a script to go through some of the well known data breaches and wordlists, collect complex passwords using the criteria mentioned and put them all in a single wordlist to be shared and used for analysis, while also making sure there weren’t duplicates. The following wordlists were used: rockyou.txt, elitehacker.txt, honeynet.txt, Ashley-Madison.txt, Lizard-Squad.txt, phpbb.txt, 000webhost.txt and NordVPN.txt

The script found 870 661 complex passwords and saved them all in a txt file called ComplexPasswords.txt which is available in the following link:
https://github.com/raskolnikov90/ComplexPassAnalysisAndWordlists/blob/main/ComplexPasswords.txt

2-Analysis of Complex Passwords Wordlist
Next, I wanted to do more analysis on the found complex passwords and made 3 scripts to do so, one would look at the most common words and combinations of letters used in the passwords, another would look at the most common suffixes of the passwords meaning anything added at the end of a password (in “Password123”, “123” would be the suffix) and another would look at the most common prefixes meaning anything added at the beginning of a password (in “!!Password”, “!!” would be the prefix). These scripts would rank them in a top 500.

We get pretty interesting yet somewhat predictable results in the top words. In top ranks we have variations of @hotmail and @yahoo meaning some people use emails frequently as passwords, the rest of the most common passwords have variations of “12345”, names, last names, the word “password”, “iloveyou” and variations of “x100pre” (forever in Spanish)
With their frequency score on the left:
https://github.com/raskolnikov90/ComplexPassAnalysisAndWordlists/blob/main/tops/wordscores.txt

Just the words without scores:
https://github.com/raskolnikov90/ComplexPassAnalysisAndWordlists/blob/main/tops/topwords.txt

The results of the suffixes where definitely interesting as it shows in its very top ranks that people most commonly use one of the numbers from 0 to 9 at the end of their password and next to them are !, 23, * and 123 as also very common suffixes. The full top 500 suffixes are available in the following links
With their frequency score on the left:
https://github.com/raskolnikov90/ComplexPassAnalysisAndWordlists/blob/main/tops/suffixscores.txt

Just the suffixes without scores:
https://github.com/raskolnikov90/ComplexPassAnalysisAndWordlists/blob/main/tops/topsuffixes.txt

The results of the prefixes where disappointing at first as the ranking is mostly compromised of letters of the alphabet and combinations of letters that are the beginning of a word, not exactly a prefix which is something you add before a word, however it was still insightful in giving confirmation that people are more likely to add something at the end of their password and not at the beginning of it so for now I didn’t do further analysis on prefixes. The full top 500 prefixes are available in the following links
With their frequency score on the left:
https://github.com/raskolnikov90/ComplexPassAnalysisAndWordlists/blob/main/tops/prefixscores.txt

Just the prefixes without scores:
https://github.com/raskolnikov90/ComplexPassAnalysisAndWordlists/blob/main/tops/topprefix.txt

3-Using Results to Generate New Complex Passwords Wordlists

I decided to use the top suffixes and top words to create new wordlists containing all possible combinations between the words and the suffixes using hashcat combinations attack mode. This created a file with 250.000 possible passwords named Motoko.txt this file is available in the following link:
https://github.com/raskolnikov90/ComplexPassAnalysisAndWordlists/blob/main/Motoko.txt

But in order to get even more variations of the newly created passwords I used hashcat again and applied the Best64 rule, this applies some of the most popular rules to generate more passwords. This created a file with 19.250.000 possible passwords named MotokoBest64.txt this file is available in the following link:
https://drive.google.com/file/d/1IcevGMAIrcmDfR-_UikFY7Eeb6UX8VzW/view?usp=drive_link

Finally, the last wordlist created combines the initial ComplexPasswords.txt and MotokoBest64.txt file into a single file called Kusanagi.txt this file is available in the following link:
https://drive.google.com/file/d/1Wk0dJsI2xFxShZ7MShxVmeQf_CjVivdz/view?usp=drive_link
 
