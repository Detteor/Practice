SET ANSI_PADDING ON
GO

USE PROD
GO

-- CREATE Table [gisadmin].[MGOPERMIT](
--   [PARCELID] [varchar](24) NOT NULL
--   ,[StructureType] [varchar](4) NOT NULL
--   ,[PermitStatus] [varchar](2)  NOT NULL
--   ,[CODate] [varchar](24) NOT NULL
--   ,[AppDate] [varchar](24) NOT NULL
--   ,[IssueDate] [varchar](24) NOT NULL
--   ,[PermitYear] [varchar](24) NOT NULL
--   ,[PermitNumber] [varchar](24) NOT NULL
--   )
TRUNCATE Table [gisadmin].[MGOPERMITS]

Insert into [gisadmin].[MGOPermits] (
    [PARCELID],
    [AppType],
    [PermitStatus],
    [CODate],
    [AppDate],
    [IssueDate],
    [PermitYear],
    [PermitNumber],
    [Designation]
)
select [PARCELID], [ApplicationType], [Status], '', '', '', '', [ProjectNumber], [Designation]
from [KCC-SQL1].[Assess50StagedData_Kent].[dbo].[MGOPermitData]

-- UPDATE [gisadmin].[PERMIT] set [gisadmin].[PERMIT].[StructureDesc] = [gisadmin].[PERMIT_Description].[StructureDesc]
-- FROM[gisadmin].[PERMIT_Description]
-- INNER JOIN [gisadmin].[PERMIT]
-- ON ( [gisadmin].[PERMIT_Description].[StructureType]=[gisadmin].[PERMIT].[StructureType] )
 


-- <End>