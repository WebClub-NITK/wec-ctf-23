# **Murder Of Timothy Thomson**

Category: Crypto

Author: Eshan Kharya

Answer / Flag: `WEC{901b44513e700e240c87aba0feb8ef2c2851e268}`

## Problem Statement

Greetings Detective Donald Duck!
Timothy Thomson the CEO of Tod and Tom Toymakers, a toy manufacturing company, was murdered in his office at 2 am on 12/03/2023 while he was working late.
There are no cctv footages, and no prime suspects. The only clues you have are:

1. A list of all 9977 employees of Tod and Tom Toymakers
2. A .jpg picture
3. A .txt file left by the murderer(s)

Your job, Detective is to find the murderers and create a string that looks like ` <id1><name1>``<id2><name2> `...`<idn><namen>`

Make sure to remove all spaces and make all the characters lowercase. Include only digits and lowercase english alphabets in your string.
Once you have this string, to completely shatter their almost shappening dreams, encode the string and create the flag.
The final answer should be provided in the given format:
WEC{`<flag>`}

Good Luck Detective!

## Relevant files / links

1. [hash.jpg](./hash.jpg)
2. [Employees.csv](./Employees.csv)
3. [ettubrutus.txt](./ettu_brutus.txt)

   [Drive link to resources](https://drive.google.com/drive/folders/1NnD4wusPY-eMtt3SR6eQ2yg0Xa5nSIUw?usp=share_link)

## Solution

1. In the ettubrutus file we find an encrypted message
   BFLNVBFLNVOFNVHPVYPHJZFHZFWONZXPLQEPCFDHSPLEDEZYPFDPOSTDWZNVLDSTDVPJZYNPQZCPLNSXFDVPEPPCPKOMRTRTEDVYAWBIVPQMYGNGTRJBEDEVGTTXTROZGBBJDNMFABYXKOEBJSRYFROZPVCDPQABQVGTTXTROZRMVFVYAWYNLBFRDEBXFTXZEZAWFPZBYWATBXAFSQXVABKEFTMKRBFSWMVF
   translates to (by applying rot11 caeser). Why caeser: Name of file. Why 11: length of file name
   QUACKQUACKDUCKWEKNEWYOUWOULDCOMEAFTERUSWHEATSTONEUSEDHISLOCKASHISKEYONCEFOREACHMUSKETEEREZDBGIGITSKNPLQXKEFBNVCVIGYQTSTKVIIMIGDOVQQYSCBUPQNMZDTQYHGNUGDOEKRSEFPQFKVIIMIGDOGBKUKNPLNCAQUGSTQMUIMOTOPLUEOQNLPIQMPUHFMKPQZTUIBZGQUHLBKU
   which means:
   QUACK QUACK DUCK WE KNEW YOU WOULD COME AFTER US WHEATSTONE USED HIS LOCK AS HIS KEY ONCE FOR EACH MUSKETEER
   EZDBGIGITSKNPLQXKEFBNVCVIGYQTSTKVIIMIGDOVQQYSCBUPQNMZDTQYHGNUGDOEKRSEFPQFKVIIMIGDOGBKUKNPLNCAQUGSTQMUIMOTOPLUEOQNLPIQMPUHFMKPQZTUIBZGQUHLBKU
2. We know Charles Wheatsone invented the playfair cipher. Lock as its key implies, the key is "playfair". Once for each musketeer implies using the key three times (as there are three musketeers (or murderes)).
   1st iteration: MUCRERERSQESFPSWHMADOURXREASSQSMURDERERTWOSAKYIWANTETFSOAKEOVERTMHCOMPANYMURDERERTHREXESFPSIWHVEQSTHNPGTSNFPNINOOPUPTHUNMAKHANTMNPDWHOWEAREX
   2nd iteration: EZBIGIGIQOKNYFQXGKFBNVCVIGYQQOTKVIIMIGDOVQQYCXBUPQNMMZQNYHGNUGDOKGRSEFPQFKVIIMIGDOGBKUKNYFNCQBUGOQQMEUMOQTYFEPTNNLNUQMNEHFHGPQMDEUBZGQUHLBKU
   3rd iteration: MURDERERONESAYSWEHADOURXREASONSMURDERERTWOSAYSIWANTEDTOTAKEOVERTHECOMPANYMURDERERTHREXESAYSIHAVENOTHINGTOSAYIUSTOPENTHEIMAGEANDFINDWHOWEAREX
3. This message can be decoded as:
   murdereronesayswehadourreasons
   murderertwosaysiwantedtotakeoverthecompany
   murdererthreesaysihavenothingtosayjustopentheimageandfindwhoweare
4. We now check the metadata of the .jpg file. In the Keywords tag we find a Base64 value.
   bT0xMDAwMzAwMDFwMT0xN3AyPTE5cDM9MjM=
   The ascii value of this is: m=100030001p1=17p2=19p3=23
5. We now use the hash function (provided in the image) on the dialogues of the murderers, with the parameters produced in the previous step
   murderer1: s = wehadourreasons p=17 m=100030001 --> 86042059
   murderer2: s = iwantedtotakeoverthecompany p=19 m=100030001 --> 70876938
   murderer1: s = ihavenothingtosayjustopentheimageandfindwhoweare p=23 m=100030001 --> 12879134
6. We search the csv file for these IDs and find the murderers to be:
   86042059: Yadiel Telly
   70876938: Katharina Cash
   12879134: Bob Rudolfo
7. We now write the string as mentioned in the format:
   86042059yadieltelly70876938katharinacash12879134bobrudolfo
   The problem statement says "shatter" their "shappening" dreams.
   SHAttered and SHAppening were two major collision attacks on the SHA1 algorithm.
   Hence we must encode this string with the SHA1 algorithm.
   This yeilds: 901b44513e700e240c87aba0feb8ef2c2851e268
8. Hence the final answer is: WEC{901b44513e700e240c87aba0feb8ef2c2851e268}
