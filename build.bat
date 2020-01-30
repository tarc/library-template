@echo off
setlocal enabledelayedexpansion


set error_message=trying cmake
where cmake > NUL 2> NUL
if NOT '%ERRORLEVEL%'=='0' goto fail


if NOT "%1"=="" (
	set build_type=%1
) else (
	set build_type=Debug
)


set script_dir=%~dp0

set build_dir=%script_dir%Multi\

for %%I in (.) do set project_name=%%~nxI

set solution=%project_name%.sln

if NOT EXIST %build_dir%%solution% (
	set error_message=calling generate

	call %script_dir%gen.bat %build_type%
	if NOT '!ERRORLEVEL!'=='0' goto fail
)


cd %build_dir%
set error_message=building
cmake --build . --config %build_type% -- /m
if NOT '!ERRORLEVEL!'=='0' goto fail


:success
	exit /b 0


:fail
	echo Something wrong during %error_message%
	exit /b 1