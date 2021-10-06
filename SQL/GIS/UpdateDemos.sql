USE [PROD]
GO

Truncate Table [gisadmin].[Demo]
Go

Insert into [gisadmin].[Demo]
	   ([PARCELID]
      ,[DemoType]
      ,[Status]
	  ,[Description])

Select
        [GMSPIN]
      ,[GBPATYP]
      ,[GBPASTS]
	  ,[GBPATNM]
      
 FROM [KCLCAS400].[S78114C0].[HTSUSR].[GISDEMO1]
GO