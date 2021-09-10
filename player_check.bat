@echo off
setlocal enabledelayedexpansion
set player_name=%~1
%player_name% >nul 2>&1
if %errorlevel% neq 0 (echo 0 >player_bool_file && exit) else (echo 1 >player_bool_file && exit)
