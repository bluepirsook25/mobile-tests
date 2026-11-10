param([string]$Url = "https://example.com", [string]$Test = "")
$env:TEST_URL = $Url
pip install -r requirements.txt
if ($Test) { pytest $Test -v --html=report.html --self-contained-html }
else       { pytest -v --html=report.html --self-contained-html }
