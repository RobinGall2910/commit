@echo off
cls
:Begin
echo Who do you think is a fuckboy?
set /p fuckboiii=
if %fuckboiii%==Robin goto Yes
cls
echo Meh, %fuckboiii% isn't a fuckboy.
goto :Begin

:Yes
cls
color c
:Loop
echo FUCKBOY ALERT
goto :Loop
