SELECT *
FROM {{ ref('fct_reviews') }} AS R
INNER JOIN {{ ref('dim_listings_cleansed') }} AS L
    ON R.LISTING_ID = L.LISTING_ID
WHERE R.REVIEW_DATE <= L.CREATED_AT
LIMIT 10