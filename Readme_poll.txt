Title :- Poll/Vote App using Django

WEBApp Link :- http://pgpoll.pythonanywhere.com/

About :- This project is a fully deployed Live web app - polling/voting application .

Overview :-
This is a voting application that displays the poll results in real-time. Each time someone votes, the application updates automatically and shows the new results.Anyone can create a poll , vote ,check results of any other poll easily ie a fully dynamic polling app.
The project is developed using django with model,view,templates architecture majorly utilising MODELFORM and meta class .
 
Django concepts involved :-  MVT, MODELFORM , Meta, CRUD , DTL ,Template Inheritance ,html render, redirect , extends ,block tag, urls , migrations.

Procedure :- 
1. The three main operations in this project are creating a poll,voting in a poll and checking results of a poll.
Also if needed one can delete a poll.
2.Every poll functions uniquely well due to default field in Django which is 'id' which is provided as a parameter to functions in views.py.
3.While creating a poll four fields are saved by model in database ; those are question,option1,option2,option3
4.Then at vote page using radiobuttons , the selected option gets saved by Django's CRUD ability in our database along with appended count/vote of option.
5.Finally , at results page we can view the results ; ie count/vote of each option displayed.
6.views.py is written for code/logic .
7.templates is used for rendering html output
8.Template inheritance is used for displaying similar layout using extends and block tag
9.Data is queried and saved from one sqlite table corresponding to the MODELFORM using Django CRUD concepts .
