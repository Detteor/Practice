USE [PROD]
GO

/****** Object:  Table [gisadmin].[PERMITS]    Script Date: 5/15/2014 3:28:16 PM ******/
DROP TABLE [gisadmin].[Restricted_Access_Citizens]
GO

/****** Object:  Table [gisadmin].[PERMITS]    Script Date: 5/15/2014 3:28:16 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

SET ANSI_PADDING ON

GO

SELECT [OBJECTID]=IDENTITY(int,1,1),
      [Map11] AS [ParcelID]
INTO GISADMIN.Restricted_Access_Citizens
FROM [KCLCAS400].[S78114C0].[HTSUSR].[MSK098PF]
GO

SET ANSI_PADDING OFF
GO
