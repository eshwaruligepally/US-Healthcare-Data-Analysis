-- Professional SQL Analysis for Billing Variance[cite: 1]

WITH PayerStats AS (
    SELECT 
        Insurance_Provider,
        AVG(Billing_Amount) OVER(PARTITION BY Insurance_Provider) as Payer_Avg,
        Billing_Amount,
        Medical_Condition
    FROM healthcare_records
)
-- Finding patients whose bills are 50% higher than their provider's average
SELECT 
    Insurance_Provider,
    Medical_Condition,
    Billing_Amount,
    Payer_Avg,
    (Billing_Amount - Payer_Avg) AS Variance
FROM PayerStats
WHERE Billing_Amount > (Payer_Avg * 1.5)
ORDER BY Variance DESC;