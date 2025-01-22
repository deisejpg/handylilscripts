USE [SalesInventoryII]
GO

SELECT 
      [ComID]
      ,[CaseID]
      ,[Format]
      ,[ResultTestName]
      ,[ResultStatusName]
      ,[ResultStatusOutput]
      ,[ResultValue]
      ,[ResultUnit]
      ,[ResultDate]
      ,[Platform]
      ,[Assay]
      ,[ResultInferenceTypeName]
      ,[ResultTestType]
      ,[SalesStatus]
      ,[StudyID]
      ,[CaseTestResults]
  FROM [dbo].[ResultsOutput]
  WHERE [CaseID] IN ('144752','150772','153256')
  AND [ResultInferenceTypeName] = 'Self'
  AND [ResultTestName] IN ('ALK');

GO