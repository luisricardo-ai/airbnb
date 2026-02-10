SELECT
    reviews.*
FROM 
    AIRBNB.DEV.FCT_REVIEWS AS reviews
INNER JOIN
    AIRBNB.DEV.dim_listings_cleansed AS listings 
    ON listings.listing_id = reviews.listing_id
WHERE
    listings.created_at > review_date
LIMIT 10