# Quick webhook test - replace YOUR_URL with your actual Render URL
 = "https://YOUR_RENDER_URL.onrender.com"

Write-Host " Quick Webhook Test" -ForegroundColor Green
Write-Host "Replace YOUR_RENDER_URL with your actual URL" -ForegroundColor Yellow

# Test basic connection
try {
     = Invoke-WebRequest -Uri "/webhook/test" -Method GET
    Write-Host " Webhooks are working! Status: " -ForegroundColor Green
     = .Content | ConvertFrom-Json
    Write-Host "Available endpoints: " -ForegroundColor Cyan
} catch {
    Write-Host " Connection failed: " -ForegroundColor Red
    Write-Host "Make sure your Render app is deployed and URL is correct" -ForegroundColor Yellow
}
