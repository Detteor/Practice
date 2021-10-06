SET ANSI_PADDING ON
GO

USE PROD
DECLARE @AS400COUNT  int;

SET @AS400COUNT = (SELECT Count([MSPIN]) FROM [KCLCAS400].[S78114C0].[HTSUSR].[BPK001P2])
Select @AS400COUNT

TRUNCATE Table [gisadmin].[PERMIT]

INSERT INTO [gisadmin].[PERMIT]
           ([PARCELID]
           ,[StructureType]
           ,[PermitStatus]
           ,[CODate]
           ,[AppDate]
           ,[IssueDate]
           ,[PermitYear]
           ,[PermitNumber])

SELECT [MSPIN]
      ,[BPATYP]
      ,[BPASTS]
      ,[BPPSTDC]
      ,[BPADATC]
	  ,[BPPISDC]
	  ,[YR]
	  ,[BPPCNB]
FROM   [KCLCAS400].[S78114C0].[HTSUSR].[BPK001P2]

UPDATE [gisadmin].[PERMIT] set [gisadmin].[PERMIT].[StructureDesc] = [gisadmin].[PERMIT_Description].[StructureDesc]
FROM[gisadmin].[PERMIT_Description]
INNER JOIN [gisadmin].[PERMIT] 
ON ( [gisadmin].[PERMIT_Description].[StructureType]=[gisadmin].[PERMIT].[StructureType] )


 DECLARE @SQLCOUNT   int;
 SET @SQLCOUNT = (SELECT Count([PARCELID]) FROM [gisadmin].[PERMIT])
 SELECT @SQLCOUNT
 
 USE msdb
  IF @SQLCOUNT <> @AS400COUNT
    EXEC sp_send_dbmail
    @profile_name = 'KCLC_Exchange',
	@recipients = 'Helpdesk@co.kent.de.us',
	@copy_recipients = 'Danielle.Lamborn@co.kent.de.us',
	@subject = 'ERIS PERMIT DB Update Error Records Total Check',
	@body = 'SQL records copied:',
	@execute_query_database = 'PROD',
	@query = 'SELECT Count([PARCELID]) FROM [gisadmin].[PERMIT]'

-- <End>