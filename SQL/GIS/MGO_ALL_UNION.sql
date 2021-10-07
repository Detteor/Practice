/****** Script for SelectTopNRows command from SSMS  ******/
--SET ANSI_PADDING ON
--GO

--USE PROD
--GO

--INSERT INTO 
select d.*
FROM (select a.PARCELID, a.AppType, a.PermitStatus, CAST(LEFT(a.AppDate, 10) as date) as AppDate, a.PermitNumber, a.IssueDate 
from gisadmin.MGOPermits as a
UNION ALL
select b.PARCELID, b.[TYPE] as [AppType], b.STATUS as [PermitStatus], b.APPDATE as AppDate, CONCAT(RIGHT(b.AppDate, 4),'-', b.PERMITNUMBER, '-', b.TYPE) as PermitNumber, CAST(b.Date as date) as IssueDate
from gisadmin.All_Permits as b) as d
ORDER BY d.PARCELID


select *
from gisadmin.MGOPermits as a
FULL JOIN gisadmin.All_Permits as b
on a.PARCELID = b.PARCELID
where a.ParcelID is not null and b.PARCELID is not null 
order by a.PARCELID

--select *
--from gisadmin.MGOPermits
--UNION ALL
--select 
--from gisadmin.All_Permits