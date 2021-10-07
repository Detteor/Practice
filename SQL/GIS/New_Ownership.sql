SELECT
    A.*
FROM 
	[BuildingValues] A (nolock)
		INNER JOIN
		(SELECT
			MAX(VersionID)As MaxVersion,
			maxVersion.[PropertyID]
		FROM
			[BuildingValues] maxVersion (nolock)
			JOIN 
			(SELECT
				MAX(YearID) AS MaxYear,
				[PropertyID]
			FROM
				[BuildingValues] (nolock)
			WHERE
                [PropertyID] = '34'
                AND [YearID] <= '2020'
			GROUP BY
				[PropertyID]
				) maxYear
			ON 
				maxVersion.PropertyID = maxYear.PropertyID and 
                maxVersion.YearID = maxYear.MaxYear
			GROUP BY 
				maxVersion.[PropertyID]
				) m 
			ON 
                m.MaxVersion = A.VersionID AND A.[ActiveFlag] = '1'















-- select max(v.YearID)
-- from Valuations v

-- select v.PropertyID, max(v.YearID), MAX(isnull(v.LandAssessedValue, 0)) as LANDASSESSMENT, MAX(isnull(v.BuildingAssessedValue, 0)) as IMPROVE, MAX(isnull(v.TotalAssessedValue, 0)) as TOTALASSESSMENT, 
-- MAX(convert(float,v.CalculatedAC)) as DEEDACREAGE
-- -- max(v.YearID), MAX(convert(float,v.CalculatedAC)) as DEEDACREAGE, 
-- -- INTO #Valuations
-- from Valuations v
-- GROUP BY v.PropertyID
-- -- JOIN Properties p ON p.PropertyID=v.PropertyID


-- select o.OwnerID, p.PARCELID as PARCELID, p.UserAccount as LOCATION, o.OwnerFormatted as OWNERNAME, o.Owner2FirstName as SECONDARYOWNER, o.StreetAddress1 as MAILINGADDRESS, o.StreetAddress2 as MAILINGADDRESS2, 
-- o.City as OWNERCITY, o.StateProvince as OWNERSTATE, o.PostalCode as OWNERZIP, max(o.YearID)
-- -- INTO #Owners
-- from Owners o, properties p
-- group by o.OwnerID, p.ParcelID
-- -- join Properties p on p.PropertyID=o.OwnerID
-- -- where p.PropertyID=o.OwnerID

-- select isnull(t.LegalReference, '') as DEEDREFERENCE, t.RecordedDate as SALESDATE
-- -- INTO #Deeds
-- from Transfers t

-- select a.AccountType as TAXEXEMPT
-- from xrAccountType a
-- join properties p on p.xrAccountTypeID=a.xrAccountTypeID

-- select max(b.YearID)
-- from Buildings b, Properties p
-- where p.PropertyID=b.PropertyID
-- b.YearBuilt as YEARBUILT, 
