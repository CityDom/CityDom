@echo off
setlocal

set "blocked_pattern=\.keystore$|\.jks$|\.p12$|\.pfx$|\.pem$|\.key$|\.mobileprovision$|\.provprofile$|^android\.keystore$|^bundle\.keystore$|^\.env$"

for /f "delims=" %%F in ('git diff --cached --name-only') do (
  echo %%F | findstr /i /r "%blocked_pattern%" >nul
  if not errorlevel 1 (
    echo Error: blocked sensitive file detected in staging area.
    echo Remove it or add to .gitignore before committing.
    exit /b 1
  )
)

exit /b 0
