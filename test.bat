@echo off
setlocal enabledelayedexpansion


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
	set error_message="Calling generate"

	call %script_dir%gen.bat %build_type%
	if NOT '!ERRORLEVEL!'=='0' goto fail
)


set error_message="Running tests"
cd %build_dir%
cmake --build . --config %build_type% -- /m
cmake --build . --config %build_type% --target RUN_TESTS
if NOT '!ERRORLEVEL!'=='0' goto fail


:success
	exit /b 0


:fail
	echo Something wrong during %error_message%
	exit /b 1
