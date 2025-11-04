# Replace YOUR_RENDER_URL with your actual Render app URL
 = "https://YOUR_RENDER_URL.onrender.com"

Write-Host " Testing Webhook Endpoints" -ForegroundColor Green
Write-Host "=================================" -ForegroundColor Green

# Test 1: Basic webhook test
Write-Host "
1. Testing basic webhook connection..." -ForegroundColor Yellow
try {
     = Invoke-WebRequest -Uri "/webhook/test" -Method GET
    Write-Host " Basic test: Status " -ForegroundColor Green
    Write-Host "Response: " -ForegroundColor Cyan
} catch {
    Write-Host " Basic test failed: " -ForegroundColor Red
}

# Test 2: Trial signup webhook
Write-Host "
2. Testing trial signup webhook..." -ForegroundColor Yellow
 = @{
    email = "test@example.com"
    name = "Test User"
    package = "free-trial"
} | ConvertTo-Json

try {
     = Invoke-WebRequest -Uri "/webhook/trial-signup" -Method POST -Body  -ContentType "application/json"
    Write-Host " Trial signup: Status " -ForegroundColor Green
    Write-Host "Response: " -ForegroundColor Cyan
} catch {
    Write-Host " Trial signup failed: " -ForegroundColor Red
}

# Test 3: Payment conversion webhook
Write-Host "
3. Testing payment conversion webhook..." -ForegroundColor Yellow
 = @{
    email = "test@example.com"
    amount = 499
    payment_id = "test_payment_20251104234957"
} | ConvertTo-Json

try {
     = Invoke-WebRequest -Uri "/webhook/trial-conversion" -Method POST -Body  -ContentType "application/json"
    Write-Host " Payment conversion: Status " -ForegroundColor Green
    Write-Host "Response: " -ForegroundColor Cyan
} catch {
    Write-Host " Payment conversion failed: " -ForegroundColor Red
}

# Test 4: Trial expired webhook
Write-Host "
4. Testing trial expired webhook..." -ForegroundColor Yellow
 = @{
    email = "test@example.com"
} | ConvertTo-Json

try {
     = Invoke-WebRequest -Uri "/webhook/trial-expired" -Method POST -Body  -ContentType "application/json"
    Write-Host " Trial expired: Status " -ForegroundColor Green
    Write-Host "Response: " -ForegroundColor Cyan
} catch {
    Write-Host " Trial expired failed: " -ForegroundColor Red
}

Write-Host "
 Webhook testing complete!" -ForegroundColor Green
Write-Host "Visit /webhook-test for interactive testing" -ForegroundColor Blue
