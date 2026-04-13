# ============================================================================
# GUIDE.TEX INTEGRITY CHECK
# ============================================================================
# Purpose: Verify that guide.tex (root) is byte-identical to the active
#          snapshot in WIP\GUIDE\ using SHA256 checksums.
# 
# Usage:   .\check-guide-integrity.ps1
# Output:  guide-integrity-check.log (always overwritten)
# ============================================================================

# Configuration
$RepoRoot = Split-Path -Parent $PSScriptRoot
$SnapshotDir = "$RepoRoot\wip\guide"
$RootGuide = "$RepoRoot\guide.tex"
$LogFile = "$RepoRoot\guide-integrity-check.log"

# Start log
$Timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$LogContent = @"
========================================
GUIDE.TEX INTEGRITY CHECK
========================================
Timestamp: $Timestamp
Repository root: $RepoRoot

"@

# Find active snapshot (only .tex file in WIP\GUIDE\)
$SnapshotFiles = Get-ChildItem -Path $SnapshotDir -Filter "*.tex" -File

if ($SnapshotFiles.Count -eq 0) {
    $LogContent += "[ERROR] No .tex file found in $SnapshotDir`n"
    $LogContent += "========================================`n"
    Set-Content -Path $LogFile -Value $LogContent
    Write-Host $LogContent -ForegroundColor Red
    exit 1
}

if ($SnapshotFiles.Count -gt 1) {
    $LogContent += "[ERROR] Multiple .tex files found in $SnapshotDir`n"
    $LogContent += "  Found: $($SnapshotFiles.Name -join ', ')`n"
    $LogContent += "  Expected: Only ONE active snapshot.`n"
    $LogContent += "========================================`n"
    Set-Content -Path $LogFile -Value $LogContent
    Write-Host $LogContent -ForegroundColor Red
    exit 1
}

$Snapshot = $SnapshotFiles[0]
$SnapshotPath = $Snapshot.FullName

# Check if root guide.tex exists
if (-not (Test-Path $RootGuide)) {
    $LogContent += "[ERROR] guide.tex not found in repository root.`n"
    $LogContent += "  Expected: $RootGuide`n"
    $LogContent += "========================================`n"
    Set-Content -Path $LogFile -Value $LogContent
    Write-Host $LogContent -ForegroundColor Red
    exit 1
}

# Get file info
$SnapshotSize = $Snapshot.Length
$RootGuideSize = (Get-Item $RootGuide).Length

$LogContent += "Active snapshot:  wip\guide\$($Snapshot.Name)`n"
$LogContent += "Canonical file:   guide.tex`n`n"
$LogContent += "Snapshot size:    $("{0:N0}" -f $SnapshotSize) bytes`n"
$LogContent += "Root size:        $("{0:N0}" -f $RootGuideSize) bytes`n`n"

# Calculate SHA256 checksums
$SnapshotHash = (Get-FileHash -Path $SnapshotPath -Algorithm SHA256).Hash
$RootHash = (Get-FileHash -Path $RootGuide -Algorithm SHA256).Hash

$LogContent += "Snapshot SHA256:  $SnapshotHash`n"
$LogContent += "Root SHA256:      $RootHash`n`n"

# Compare
if ($SnapshotHash -eq $RootHash) {
    $LogContent += "[PASS] FILES ARE IDENTICAL`n"
    $LogContent += "  Snapshot and guide.tex match perfectly.`n"
    $LogContent += "========================================`n"
    Set-Content -Path $LogFile -Value $LogContent
    Write-Host $LogContent -ForegroundColor Green
    exit 0
} else {
    $LogContent += "[FAIL] FILES ARE DIFFERENT`n"
    $LogContent += "  WARNING: guide.tex does not match the active snapshot!`n`n"
    $LogContent += "  ACTION REQUIRED:`n"
    $LogContent += "  Copy wip\guide\$($Snapshot.Name) to guide.tex`n`n"
    $LogContent += "  Command:`n"
    $LogContent += "  Copy-Item `"$SnapshotPath`" -Destination `"$RootGuide`" -Force`n"
    $LogContent += "========================================`n"
    Set-Content -Path $LogFile -Value $LogContent
    Write-Host $LogContent -ForegroundColor Red
    exit 1
}