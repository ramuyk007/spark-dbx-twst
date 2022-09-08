@rem Name: Powershell execution policy workaround tool
@rem Usage: Drop this file next to a powershell '.ps1' file and rename it to 
@rem      : the same name as the powershell file. 
@rem      : e.g. Put it next to "go.ps1" and rename to "go.bat" then it will 
@rem      : call "go.ps1" file.
@rem Notes: Bulk of solution comes from: https://www.netspi.com/blog/technical/network-penetration-testing/15-ways-to-bypass-the-powershell-execution-policy/
@rem Known Issue: Only 9 parameters can be passed to the powershell function
@echo PEPWT: Starting Powershell Execution Policy Workaround Tool (PEPWT)
@PowerShell.exe -NoProfile -Command "function Disable-ExecutionPolicy{($ctx = $executioncontext.gettype().getfield('_context','nonpublic,instance').getvalue( $executioncontext)).gettype().getfield('_authorizationManager','nonpublic,instance').setvalue($ctx, (new-object System.Management.Automation.AuthorizationManager 'Microsoft.PowerShell'))}; Disable-ExecutionPolicy; Write-Host 'PEPWT: Executing: %~dpn0.ps1 %1 %2 %3 %4 %5 %6 %7 %8 %9'; & '%~dpn0.ps1' %1 %2 %3 %4 %5 %6 %7 %8 %9"
@echo PEPWT: exitcode = %ERRORLEVEL%