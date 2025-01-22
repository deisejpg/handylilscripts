Get-ChildItem -Path . -Recurse -Filter *.xlsx | ForEach-Object {
 try {
 $excel = New-Object -ComObject Excel.Application
 $workbook = $excel.Workbooks.Open($excelFile)
 foreach ($sheet in $workbook.Sheets) {
 $range = $sheet.UsedRange
 if ($range.Text -like "*find_string*") {
                 Write-Host "Found 'find_string' in file: $excelFile on sheet: $($sheet.Name)"
             }
         }
         $workbook.Close($false)
         $excel.Quit()
     } catch {
         Write-Host "Error processing file: $excelFile"
     }
 }
