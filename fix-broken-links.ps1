# Fix broken navigation links in all HTML files
# Problems:
# 1. News links broken: href="\news/" (with newline) → href="news/"
# 2. About links missing "a": href="bout/" → href="about/"
# 3. Breadcrumb links missing ">": href="../index.html"Home → href="../index.html">Home
# 4. Logo links format error: href="..."class="logo" → href="..."> class="logo"

$rootDir = "C:\Users\ymlt\Desktop\vicor"

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "Vicor Website Link Repair Tool" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Root directory: $rootDir" -ForegroundColor Gray
Write-Host ""

# Get all HTML files
$htmlFiles = Get-ChildItem -Path $rootDir -Filter "*.html" -Recurse

Write-Host "Found $($htmlFiles.Count) HTML files to process" -ForegroundColor Green
Write-Host ""

# Counters
$totalFiles = 0
$filesModified = 0
$newsFixed = 0
$aboutFixed = 0
$breadcrumbFixed = 0
$logoFixed = 0

foreach ($file in $htmlFiles) {
    $totalFiles++
    Write-Host "[$totalFiles/$($htmlFiles.Count)] Processing: $($file.Name)" -ForegroundColor Yellow

    # Read file content
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    $changes = @()

    # 1. Fix News navigation links (remove newlines between / and ews/)
    $newsPattern = 'href="([\.\/]*?)[\r\n]+ews/'
    if ($content -match $newsPattern) {
        $beforeCount = ([regex]::Matches($content, $newsPattern)).Count
        $content = $content -replace $newsPattern, 'href="$1news/'
        $newsFixed += $beforeCount
        $changes += "News links: $beforeCount"
    }

    # 2. Fix About navigation links (add missing "a")
    $aboutPattern = 'href="([\.\/]*?)bout/'
    if ($content -match $aboutPattern) {
        $beforeCount = ([regex]::Matches($content, $aboutPattern)).Count
        $content = $content -replace $aboutPattern, 'href="$1about/'
        $aboutFixed += $beforeCount
        $changes += "About links: $beforeCount"
    }

    # 3. Fix breadcrumb links (add missing ">")
    $breadcrumbPattern = '(href="[^"]*?index\.html)"([A-Z])'
    if ($content -match $breadcrumbPattern) {
        $beforeCount = ([regex]::Matches($content, $breadcrumbPattern)).Count
        $content = $content -replace $breadcrumbPattern, '$1">$2'
        $breadcrumbFixed += $beforeCount
        $changes += "Breadcrumb links: $beforeCount"
    }

    # 4. Fix logo links (add ">" and space)
    $logoPattern = '(href="[^"]*?")class="logo"'
    if ($content -match $logoPattern) {
        $beforeCount = ([regex]::Matches($content, $logoPattern)).Count
        $content = $content -replace $logoPattern, '$1 class="logo"'
        $logoFixed += $beforeCount
        $changes += "Logo links: $beforeCount"
    }

    # Write back if changes were made
    if ($content -ne $originalContent) {
        $content | Set-Content -Path $file.FullName -Encoding UTF8 -NoNewline
        $filesModified++
        Write-Host "  ✓ Fixed: $($changes -join ', ')" -ForegroundColor Green
    } else {
        Write-Host "  - No changes needed" -ForegroundColor Gray
    }

    Write-Host ""
}

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "  Files processed: $totalFiles" -ForegroundColor White
Write-Host "  Files modified: $filesModified" -ForegroundColor Green
Write-Host "" -ForegroundColor White
Write-Host "  News links fixed: $newsFixed" -ForegroundColor Green
Write-Host "  About links fixed: $aboutFixed" -ForegroundColor Green
Write-Host "  Breadcrumb links fixed: $breadcrumbFixed" -ForegroundColor Green
Write-Host "  Logo links fixed: $logoFixed" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Cyan
