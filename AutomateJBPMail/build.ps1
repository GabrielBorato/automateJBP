$exclude = @("venv", "automateMail.JBP.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "automateMail.JBP.zip" -Force