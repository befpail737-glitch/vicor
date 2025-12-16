# Fix image extensions from .jpg to .svg in all HTML files
# Problem: All .jpg files are actually SVG files, causing images not to load

$rootDir = "C:\Users\ymlt\Desktop\vicor"

Write-Host "Starting image extension fix..." -ForegroundColor Cyan
Write-Host "Root directory: $rootDir" -ForegroundColor Gray
Write-Host ""

# Get all HTML files
$htmlFiles = Get-ChildItem -Path $rootDir -Filter "*.html" -Recurse

Write-Host "Found $($htmlFiles.Count) HTML files to process" -ForegroundColor Green
Write-Host ""

# Counter for tracking changes
$totalChanges = 0
$filesModified = 0

# List of image filenames to replace (without extension)
$imageNames = @(
    "dcm-module",
    "bcm-module",
    "prm-module",
    "vtm-module",
    "aerospace-solution",
    "automotive-solution",
    "robotics-solution",
    "rail-solution",
    "thomas-wang",
    "jennifer-liu",
    "robert-chen",
    "application-note",
    "beijing-support-center",
    "chip-packaging",
    "company-news",
    "faq-overview",
    "faq",
    "industry-news",
    "input-filter",
    "news-header-generic",
    "news-header",
    "packaging-technology",
    "picor-ic",
    "power-system-architecture",
    "selection-guide",
    "thermal-design-guide",
    "thermal-design"
)

foreach ($file in $htmlFiles) {
    Write-Host "Processing: $($file.Name)" -ForegroundColor Yellow

    # Read file content
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    $fileChanges = 0

    # Replace each image from .jpg to .svg
    foreach ($imageName in $imageNames) {
        $pattern = "$imageName\.jpg"
        $replacement = "$imageName.svg"

        if ($content -match $pattern) {
            $content = $content -replace $pattern, $replacement
            $matches = ([regex]::Matches($originalContent, $pattern)).Count
            $fileChanges += $matches
            Write-Host "  - Replaced $matches occurrence(s) of '$pattern'" -ForegroundColor Gray
        }
    }

    # Write back if changes were made
    if ($fileChanges -gt 0) {
        $content | Set-Content -Path $file.FullName -Encoding UTF8 -NoNewline
        $totalChanges += $fileChanges
        $filesModified++
        Write-Host "  ✓ $fileChanges replacement(s) made" -ForegroundColor Green
    } else {
        Write-Host "  - No changes needed" -ForegroundColor Gray
    }

    Write-Host ""
}

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "  Files processed: $($htmlFiles.Count)" -ForegroundColor White
Write-Host "  Files modified: $filesModified" -ForegroundColor Green
Write-Host "  Total replacements: $totalChanges" -ForegroundColor Green
Write-Host "===============================================" -ForegroundColor Cyan
