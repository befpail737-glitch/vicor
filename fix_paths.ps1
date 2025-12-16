# Powershell script to fix relative paths in Vicor project files
# The issue: files in subdirectories like products/modular-power/dcm/high-power/
# should use "../../../" to reach root, not "../../../../"

$files = @(
    "products\modular-power\dcm\high-power\index.html",
    "products\modular-power\dcm\low-profile\index.html",
    "products\modular-power\dcm\automotive\index.html",
    "products\modular-power\dcm\aerospace\index.html",
    "products\modular-power\bcm\high-power\index.html",
    "products\modular-power\prm\high-power\index.html",
    "products\modular-power\vtm\high-power\index.html",
    "products\input-filter\emi-filters\index.html",
    "products\picor\power-controllers\index.html"
)

foreach ($file in $files) {
    $fullPath = Join-Path "C:\Users\ymlt\Desktop\vicor" $file
    
    if (Test-Path $fullPath) {
        Write-Host "Processing $fullPath"
        
        # Read the content
        $content = Get-Content $fullPath -Raw
        
        # Replace all instances of ../../../../ with ../../../
        $newContent = $content -replace '\.\./\.\./\.\./\.\./', '../../../'
        
        # Special handling for files already in the right location (one level deep from root)
        # For these, we want to go up 2 levels: ../../
        # But looking at the structure, all our files are 3 levels deep: products/x/y/
        # So ../../../ is correct to reach root
        
        # Write the updated content back
        Set-Content -Path $fullPath -Value $newContent
        
        Write-Host "  Fixed paths in $file"
    }
    else {
        Write-Host "  File not found: $fullPath"
    }
}

Write-Host "Path fixing complete!"