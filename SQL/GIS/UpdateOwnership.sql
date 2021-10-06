SET ANSI_PADDING ON
GO

USE [PROD]
DECLARE @ASSESS50  int;

SET @ASSESS50 = (SELECT Count([PARCELID]) FROM [KCC-SQL1].[Assess50Kent].[dbo].[OWNERSHIPN])
Select @ASSESS50

TRUNCATE Table [gisadmin].[OWNERSHIPINFORMATION]

INSERT INTO [gisadmin].[OWNERSHIPINFORMATION]
           ([PARCELID]
           ,[LOCATION]
           ,[OWNERNAME]
           ,[SECONDARYOWNER]
           ,[MAILINGADDRESS]
           ,[MAILINGADDRESS2]
           ,[OWNERCITY]
           ,[OWNERSTATE]
           ,[OWNERZIP]
           ,[DEEDREFERENCE]
           ,[DEEDACREAGE]
           ,[LANDASSESSMENT]
           ,[IMPROVE]
           ,[TOTALASSESSMENT]
           ,[LOCATIONID]
           ,[TaxExempt]
           ,[YearBuilt]
            ,[PROPERTYUSE]
			,[SALESDATES])

SELECT [PARCELID] AS [PARCELID]
      ,[EXPROP] AS [LOCATION]
      ,[OWNERNAME] AS [OWNERNAME]
      ,[AGAETX] AS [SECONDARYOWNER]
      ,[EXOWN1] AS [MAILINGADDRESS]
      ,[EXOWN2] AS [MAILINGADDRESS2]
      ,[OWNERCITY] AS [OWNERCITY]
      ,[OWNERSTATE] AS [OWNERSTATE]
      ,[OWNERZIP] AS [OWNERZIP]
      ,[EXDBVP] AS [DEEDREFERENCE]
	  ,[XXGTLS] AS [DEEDACREAGE]
	  ,[XXLLND] AS [LANDASSESSMENT]
	  ,[XXLIMP] AS [IMPROVE]
	  ,[XXLTOT] AS [TOTALASSESSMENT]
      ,[LOCATION] AS [LOCATIONID]
	  ,[AJBDCD] AS [TaxExempt]
	  ,[XXYRBL] AS [YearBuilt]      
      ,[PUSEDESC] AS [PROPERTYUSE]
	  ,[SALEDATES] AS [SALEDATE]
                  
  FROM [KCC-SQL1].[Assess50Kent].[dbo].[OWNERSHIPN]

delete from [gisadmin].[OWNERSHIPINFORMATION]
where [PARCELID]in (select [ParcelID] from [gisadmin].[RESTRICTED_ACCESS_CITIZENS])