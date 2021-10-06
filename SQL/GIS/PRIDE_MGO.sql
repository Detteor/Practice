select distinct max(format(cast(right(a.APPDATE, 4) as date), 'yyyy')) as PermitYear, a.PARCELID,a.PERMITNUMBER, a.[TYPE], a.[STATUS]
from prod.gisadmin.All_Permits as a
where ([TYPE] = 'SFD' or [TYPE] = 'SFA' or [TYPE] = 'SFD' or [TYPE] =  'MANH' or [TYPE]= 'MHRP' or [TYPE]= 'MHPS')
group by PARCELID, PERMITNUMBER, [TYPE], [STATUS]
order by PARCELID


select c.PARCELID, format(cast(right(c.APPDATE, 4) as date), 'yyyy') as PermitYear
from (select a.PARCELID, max(format(cast(right(a.APPDATE, 4) as date), 'yyyy')) as PermitYear
from gisadmin.All_Permits as a
--where a.[TYPE] = 'SFD' or a.[TYPE] = 'SFA' or a.[TYPE] = 'SFD' or a.[TYPE] =  'MANH' or a.[TYPE]= 'MHRP' or a.[TYPE]= 'MHPS'
--where PARCELID = '1-00-00300-01-1600-00001'
GROUP BY a.PARCELID
) as b
join gisadmin.All_Permits as c
on b.PARCELID = c.PARCELID and b.PermitYear=format(cast(right(c.APPDATE, 4) as date), 'yyyy')
order by c.PARCELID