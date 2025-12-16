# Fix absolute paths in HTML files to relative paths
$rootDir = "C:\Users\ymlt\Desktop\vicor"

# Function to calculate relative path prefix based on depth
function Get-RelativePrefix {
    param($depth)
    if ($depth -eq 0) { return "" }
    return ("../" * $depth)
}

# Function to get directory depth
function Get-DirectoryDepth {
    param($filePath, $rootPath)
    $relativePath = $filePath.Substring($rootPath.Length).TrimStart('\')
    $parts = $relativePath.Split('\')
    return ($parts.Length - 1)  # Subtract 1 for the file itself
}

# Find all HTML files
$htmlFiles = Get-ChildItem -Path $rootDir -Filter "*.html" -Recurse

Write-Host "Found $($htmlFiles.Count) HTML files to process"

foreach ($file in $htmlFiles) {
    Write-Host "Processing: $($file.FullName)"

    # Calculate depth
    $depth = Get-DirectoryDepth -filePath $file.FullName -rootPath $rootDir
    $prefix = Get-RelativePrefix -depth $depth

    # Read file content
    $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8

    # Replace absolute paths with relative paths
    # Images
    $content = $content -replace 'src="/images/', "src=""$prefix`images/"
    $content = $content -replace 'href="/images/', "href=""$prefix`images/"

    # CSS
    $content = $content -replace 'href="/css/', "href=""$prefix`css/"

    # JS
    $content = $content -replace 'src="/js/', "src=""$prefix`js/"

    # Links to pages (but not root /)
    $content = $content -replace 'href="/products/', "href=""$prefix`products/"
    $content = $content -replace 'href="/solutions/', "href=""$prefix`solutions/"
    $content = $content -replace 'href="/support/', "href=""$prefix`support/"
    $content = $content -replace 'href="/news/', "href=""$prefix`news/"
    $content = $content -replace 'href="/about/', "href=""$prefix`about/"
    $content = $content -replace 'href="/contact/', "href=""$prefix`contact/"
    $content = $content -replace 'href="/privacy-policy/', "href=""$prefix`privacy-policy/"
    $content = $content -replace 'href="/terms-of-service/', "href=""$prefix`terms-of-service/"
    $content = $content -replace 'href="/cookie-policy/', "href=""$prefix`cookie-policy/"
    $content = $content -replace 'href="/resources/', "href=""$prefix`resources/"

    # Fix home links based on depth
    if ($depth -eq 0) {
        # Root level - keep as is or use index.html
        $content = $content -replace 'href="/"([^a-zA-Z])', 'href="index.html"$1'
    } else {
        # Subdirectory - use relative path to root
        $content = $content -replace 'href="/"([^a-zA-Z])', "href=""$prefix`index.html""$1"
    }

    # Write back to file
    $content | Set-Content -Path $file.FullName -Encoding UTF8 -NoNewline

    Write-Host "  Depth: $depth, Prefix: '$prefix'"
}

Write-Host "`nCompleted processing all HTML files!"
