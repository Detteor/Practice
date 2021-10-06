USE [PROD]
GO

Truncate Table [gisadmin].[violations]
Go

Insert into [gisadmin].[violations]
	   ([PARCELID]
      ,[VIOLATIONTYPE]
      ,[VIOLATIONSTATUS]
	  ,[VIOLATIONDESC])

Select
       [MSPIN]
      ,[CECTCD]
      ,[CECSTS]
	  ,''
      
  FROM [KCLCAS400].[S78114C0].[HTSUSR].[BPK001P3]
GO
update [gisadmin].[violations] set [gisadmin].[violations].[VIOLATIONDESC] = [gisadmin].[violations_description].[VIOLATIONDESC]
FROM[gisadmin].[violations_description]
INNER JOIN [gisadmin].[violations]
ON ([gisadmin].[violations_description].[VIOLATIONTYPE] = [gisadmin].[violations].[VIOLATIONTYPE])
GO