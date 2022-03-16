def display_original_purchase_history(original_purchase_df, customer_id, limit_top_rows=5):
    original_purchases = original_purchase_df.loc[original_purchase_df["CustomerID"] == customer_id]
    original_purchases = original_purchases[
        ["CustomerID", "StockCode", "Description", "Quantity", "Invoice", "InvoiceDate"]
    ]
    display(
        md(
            "**[ <u>Top {} Original Purchase History</u> ] for a Customer ID : {}**".format(
                limit_top_rows, customer_id
            )
        )
    )
    return original_purchases.head(limit_top_rows).style.hide_index()