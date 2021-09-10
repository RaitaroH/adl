@echo off
setlocal enabledelayedexpansion
set player_name=%~1

where /q %player_name%
if %errorlevel% neq 0 (call :player_notpresent) else (call :player_present)
:player_present
rem Present
echo 1 >player_bool_file
exit
:player_notpresent
rem Present
echo 0 >player_bool_file
exit
