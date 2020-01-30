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

set app=%project_name%.exe

if NOT EXIST %build_dir%%build_type%\%app% (
	set error_message=calling build

	call %script_dir%build.bat %build_type%
	if NOT '!ERRORLEVEL!'=='0' goto fail
)


set error_message="%app%"
cd %build_dir%
cmake --build . --config %build_type% --target run
if NOT '!ERRORLEVEL!'=='0' goto fail


:success
	exit /b 0


:fail
	echo Something wrong during %error_message%
	exit /b 1