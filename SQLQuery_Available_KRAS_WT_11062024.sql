USE [SalesInventoryII]
GO

SELECT  [Case ID]
       ,[Com ID]
       ,[Format]
       ,[Tissue]
       ,[Sales Status]
	   ,[SubFormat]
	   ,[Tissue Diagnosis]
	   ,[FormatPortal]
	   ,[SubformatPortal]
	   ,[DiseaseGroupPortal]
	   ,[Biosample Confirmed Diagnosis]
	   ,[Primary Diagnosis]
	   ,[Biosample Confirmed Sub-Diagnosis]
	   ,[Tumor Grade]
	   ,[Metastatic Site Of Orgin]
	   ,[Mutation Test Results]
	   ,[Significant Variant Positive]
	   ,[Significant Variant Wildtype]
	   ,[Fusion Positive]
	   ,[Fusion Wildtype]
	   ,[CNV Abnormal]
	   ,[CNV Normal]
	   
      
  FROM [dbo].[SalesInventorySearchAllPostAperio]
  WHERE [Significant Variant Wildtype] IS NOT NULL
  AND LEN([Significant Variant Wildtype]) > 0 -- Exclude empty strings
  AND [Significant Variant Wildtype] LIKE '%KRAS%' -- Check for "KRAS" or "KRAS:Neg"
  AND [Tissue Diagnosis] = 'Tumor'
  AND [Sales Status] = '1'
  AND [Format] IN ('FFPE','Fresh Frozen','OCT Embed')
  
  
GO