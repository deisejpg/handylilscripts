USE [SalesInventoryII]
GO

SELECT localView.[Case ID]
	   ,localView.[Country of Collection Site]
	   ,localView.[Com ID]
	   ,localView.[Specimen ID]
	   ,localView.[Format]
	   ,localView.[Tissue]
	   ,localView.[H&E Image Link 20x]
	   ,localView.[Whole Slide Image]
	  
	   ,remoteViewA.[ComID]
	   ,remoteViewA.[ImageId]
	   ,remoteViewA.[SlideID]
	   ,remoteViewA.[ServerLocation]
	   ,remoteViewA.[ImageGuid]
	   ,remoteViewA.[ISLegacy]
	   
	   ,remoteViewB.[ImageID]
       ,remoteViewB.[Magnification]

			FROM [dbo].[SalesInventorySearchAllPostAperio] AS localView
			
			-- full outer join to get everything from localview that matches the conditions below
			FULL OUTER JOIN [aperio_server_upgrade].[AperioIntegrationObjects].[dbo].[ImageLookup] AS remoteViewA 
				ON localView.[Com ID] = remoteViewA.[ComID]
			FULL OUTER JOIN [aperio_server_upgrade].[AperioIntegrationObjects].[dbo].[ImageMetaData] AS remoteViewB
				ON remoteViewA.[ImageId] = remoteViewB.[ImageID]

			-- selecting only Asian and European countries
			--WHERE UPPER(localView.[Country of Collection Site]) NOT IN ('Unknown')
			---- selecting all possible names for HE slides in the format column
			--AND localView.[Format] IN ('H&E Slide','HE','HECustom')
			WHERE localView.[Format] IN ('H&E Slide','HE','HECustom','ER', 'HER2', 'IHC', 'PR', 'Unstained')
			-- selecting everything that is not null in slide image columns of interest
			AND (localView.[Whole Slide Image] IS NOT NULL
			OR localView.[H&E Image Link 20x] IS NOT NULL)

			 
GO
