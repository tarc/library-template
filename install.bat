@echo off
setlocal enabledelayedexpansion


set error_message=trying conan
where conan > NUL 2> NUL
if NOT '%ERRORLEVEL%'=='0' goto fail


set error_message=trying cmake
where cmake > NUL 2> NUL
if NOT '%ERRORLEVEL%'=='0' goto fail


set script_dir=%~dp0

set gen_dir=%script_dir%Multi\

if EXIST %gen_dir% (
	set error_message="rmdir /s/q %gen_dir%"
	rmdir /s/q %gen_dir%
	if NOT '!ERRORLEVEL!'=='0' goto fail
)


set error_message="mkdir %gen_dir%"
mkdir %gen_dir%
if NOT '!ERRORLEVEL!'=='0' goto fail

pushd %gen_dir%


set error_message="conan install .. -g cmake_multi"

conan install .. -g cmake_multi -s arch=x86_64 -s build_type=Release -s compiler.runtime=MT -s compiler.version=16 --build=missing
if NOT '%ERRORLEVEL%'=='0' goto fail 

conan install .. -g cmake_multi -s arch=x86_64 -s build_type=Debug -s compiler.runtime=MTd -s compiler.version=16 --build=missing
if NOT '%ERRORLEVEL%'=='0' goto fail 


set generator=Visual Studio 16 2019

set error_message="cmake .. -G "%generator%" -DMULTI_CONFIG=ON -A x64"
cmake .. -G "%generator%" -DMULTI_CONFIG=ON -A x64

if NOT '%ERRORLEVEL%'=='0' goto fail 


:success
	exit /b 0


:fail
	echo Something wrong during %error_message%
	exit /b 1
