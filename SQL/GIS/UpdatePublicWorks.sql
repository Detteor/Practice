USE [PublicWorks]
GO

DROP TABLE [pwadmin].[TRASH]
GO          
           
    SELECT 
	[OBJECTID]=IDENTITY(int,1,1)
      ,[MSPIN] AS [PARCELID]
      ,[EXTRSH] AS [DIS]
      ,[TRSHVAL] AS [UNIT]

	  INTO [pwadmin].[TRASH]

     FROM [KCLCAS400].[S78114C0].[HTSUSR].[TRASH]
           
GO

DROP TABLE [pwadmin].[STREETLIGHT]
GO
           
    SELECT 
	[OBJECTID]=IDENTITY(int,1,1)
      ,[MSPIN] AS [PARCELID]
      ,[EXLIGT] AS [DIS]
      ,[LIGTVAL] AS [UNITS]

	 INTO [pwadmin].[STREETLIGHT]
          

     FROM [KCLCAS400].[S78114C0].[HTSUSR].[LIGHT]
           
GO