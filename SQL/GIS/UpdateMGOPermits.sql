SET ANSI_PADDING ON
GO

USE PROD





SELECT b.ProjectNumber
  FROM dbo.MGOPermitFees a
  join dbo.MGOPermitData b on (a.PermitID=b.MPNPermitID)
  where (b.ProjectNumber LIKE '%DEMO' or b.ProjectNumber LIKE '%DEMS' or b.ProjectNumber LIKE '%MHDM')
--   a.IsIssued = 1
--   (b.ProjectNumber LIKE '%SFD' or b.ProjectNumber LIKE '%SFA' or b.ProjectNumber LIKE '%MANH' or b.ProjectNumber LIKE '%MHRP' or b.ProjectNumber like '%MHPS')
-- select *
-- from dbo.MGOPermitData
-- where MPNPermitID = 4448508 
-- select a.Created, b.IssuedDate
-- from dbo.MGOPermitFees b
-- join dbo.MGOPermitData a on (b.PermitID = a.MPNPermitID)
-- where b.IsIssued = 1 and b.IssuedDate IS NOT NULL
-- order by b.PermitID