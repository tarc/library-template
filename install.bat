@echo off
setlocal enabledelayedexpansion


set error_message=trying conan
where conan > NUL 2> NUL
if NOT '%ERRORLEVEL%'=='0' goto fail


set error_message=trying cmake
where cmake > NUL 2> NUL
if NOT '%ERRORLEVEL%'=='0' goto fail


if NOT "%1"=="" (
	set tmp=%1
) else (
	set tmp=tmp
)


set script_dir=%~dp0

set gen_dir=%script_dir%%tmp%\

if EXIST %gen_dir% (
	set error_message="rmdir /s/q %gen_dir%"
	rmdir /s/q %gen_dir%
	if NOT '!ERRORLEVEL!'=='0' goto fail
)


set error_message="mkdir %gen_dir%"
mkdir %gen_dir%
if NOT '!ERRORLEVEL!'=='0' goto fail

cd %gen_dir%


set error_message="conan install .. --build=missing"
conan install .. --build=missing
if NOT '%ERRORLEVEL%'=='0' goto fail 


:success
	exit /b 0


:fail
	echo Something wrong during %error_message%
	exit /b 1
