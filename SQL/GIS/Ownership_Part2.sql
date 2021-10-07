-- Step 4 of job
select b.PropertyID,
	sum(isnull(TotalAppraisedValue, 0)) as TotalAppraisedValue
	--max(isnull(
From GetValuationsTable('2020','1') b
where xrValuationOptionID = 1 or xrValuationOptionID = 16
Group by b.PropertyID

