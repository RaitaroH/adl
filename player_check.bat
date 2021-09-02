@echo off
setlocal enabledelayedexpansion
mpv >nul 2>&1
if %errorlevel% neq 0 (call :player_notpresent) else (call :player_present)
:player_present
rem Present
echo 1 >player_bool
exit
:player_notpresent
rem Present
echo 0 >player_bool
exit