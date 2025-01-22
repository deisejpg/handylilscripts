USE [dbII]
GO

SELECT localView.[Case ID]
	   ,localView.[Com ID]
	   ,localView.[Specimen ID]
	   ,localView.[Species]
	   ,localView.[Format]
	   ,localView.[Tissue]
	   ,localView.[Tissue Diagnosis]
	   ,localView.[Biosample Confirmed Diagnosis]
	   ,localView.[Primary Diagnosis]
	   ,localView.[Biosample Confirmed Sub-Diagnosis]
	   ,localView.[Metastatic Site Of Orgin]
	   ,localView.[Whole Slide Image]
	   ,localView.[Age at Excision]
	   ,localView.[Age At Excision]
       ,localView.[Age]
       ,localView.[AgeUnit]
       ,localView.[Sex]
       ,localView.[Excision Year]
	   ,remoteView.[ComID]
	   ,remoteView.[ImageId]
	   ,remoteView.[SlideID]
	   ,remoteView.[ServerLocation]
	   ,remoteView.[ImageGuid]
	   ,remoteView.[ISLegacy]
	   
			FROM [dbo].[SearchAll] AS localView
 
			INNER JOIN [server].[IntegrationObjects].[dbo].[ImageLookup] AS remoteView
 
			ON localView.[Com ID] = remoteView.[ComID]
  
			WHERE remoteView.[ImageId] in ('444444','555555','666666')
			
 
GO


